from django.shortcuts import render
import requests
# For generation of a new auth token
import json
import secrets
#Bringing in Models
from signup.models import userprofile
from animelist.models import AnimeEntry
from mangalist.models import MangaEntry

# Page Renders
def animelist(request):
    user = userprofile.objects.get(username = request.user)
    if (request.method == 'GET') and ('code' in request.GET):
        auth_code = request.GET['code']
        token = generate_new_token(auth_code, user.refresh_token)
        user.access_token = token['access_token']
        user.refresh_token = token['refresh_token']
        user.has_mal = True
        user.save()
        populate_animelist(user.access_token, user)
        return render(request, 'animelist/animelist.html', {"user":user})
    if not user.has_mal:
        code_challenge = get_new_code_verifier()
        url = return_new_authorisation_url(code_challenge)
        user.refresh_token = code_challenge
        user.save()
        context = {
            "connect_mal_url": url
        }
        return render(request, 'animelist/animelist_empty.html', context)
    return render(request, 'animelist/animelist.html', {"user":user})


# Helper Functions to generate auth token (from ZeroCrystal)
CLIENT_ID = '03c7b68db12e88a5a326d3ca331d42a8'
CLIENT_SECRET = '1372d641a42033f35b4474b16d492e0f1a38eb2e14ac691ec48f69720fa6da10'

def get_new_code_verifier() -> str:
    """
    Returns a randon 128 sequence as a secret
    """
    token = secrets.token_urlsafe(100)
    return token[:128]

def return_new_authorisation_url(code_challenge: str):
    """
    Returns the url to authorize mConnect
    """
    global CLIENT_ID
    url = f'https://myanimelist.net/v1/oauth2/authorize?response_type=code&client_id={CLIENT_ID}&code_challenge={code_challenge}'
    return url

def generate_new_token(authorisation_code: str, code_verifier: str) -> dict:
    """
    Creates a MAL token and returns it
    """
    global CLIENT_ID, CLIENT_SECRET
    url = 'https://myanimelist.net/v1/oauth2/token'
    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': authorisation_code,
        'code_verifier': code_verifier,
        'grant_type': 'authorization_code'
    }
    response = requests.post(url, data)
    response.raise_for_status()  # Check whether the requests contains errors
    token = response.json()
    response.close()
    return token

# Helper Functions to grab animelist
def get_animelist(access_token: str):
    """
    Returns the animelist of a user with a limit of 4
    """
    url = f'https://api.myanimelist.net/v2/users/@me/animelist?fields=list_status&limit=4'
    response = requests.get(url, headers= {
        'Authorization': f'Bearer {access_token}'
    })
    response.raise_for_status()
    anime_list = response.json()
    response.close()
    return anime_list

def get_animeinfo(access_token: str, anime_id: int):
    """
    Returns a dictionary of the anime information
    """
    url = f'https://api.myanimelist.net/v2/anime/{anime_id}?fields=id,title,main_picture,alternative_titles,start_date,end_date,synopsis,mean,rank,popularity,num_list_users,num_scoring_users,nsfw,created_at,updated_at,media_type,status,genres,my_list_status,num_episodes,start_season,broadcast,source,average_episode_duration,rating,pictures,background,related_anime,related_manga,recommendations,studios,statistics'
    response = requests.get(url, headers= {
        'Authorization': f'Bearer {access_token}'
    })
    response.raise_for_status()
    anime_stats = response.json()
    response.close()
    return anime_stats

def populate_animelist(access_token: str, user: userprofile):
    """
    Populates a user's animelist using their MAL information
    """
    animelist = get_animelist(access_token)['data']
    for i in animelist:
        info = i['node']
        status_M = i['list_status']
        # Defining Intial Params
        mal_id = info['id']
        title = info['title']
        eps = status_M['num_watched_episdoes']
        status = status_M['status']
        score = status_M['score']
        rating = ...
        picture = info['main_picture']['large']
        rewatching = status_M['is_rewatching']
        rewatched = ...
        comments = ...
        prio = ...
        # Intialization of Anime Entry
        anime_entry = AnimeEntry(mal_id = mal_id, title = title, eps = eps, status = status, score = score, rating = rating, picture = picture, rewatching = rewatching, rewatched = rewatched, comments = comments, prio = prio)
        anime_entry.save()
        # Adding to user animelist

