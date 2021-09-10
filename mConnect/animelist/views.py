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
        user.save()
        populate_animelist(user.access_token, user)
        user.has_mal = True
        user.save()
        anime_list = user.animeentry_set.all()
        context = {
            'user': user,
            'animelist': anime_list
        }
        return render(request, 'animelist/animelist.html', context)
    if not user.has_mal:
        code_challenge = get_new_code_verifier()
        url = return_new_authorisation_url(code_challenge)
        user.refresh_token = code_challenge
        user.save()
        context = {
            "connect_mal_url": url
        }
        return render(request, 'animelist/animelist_empty.html', context)
    populate_animelist(user.access_token, user)
    anime_list = user.animeentry_set.all()
    context = {
        'user': user,
        'animelist': anime_list
    }
    return render(request, 'animelist/animelist.html', context)


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
    url = f'https://api.myanimelist.net/v2/users/@me/animelist?fields=list_status&limit=100'
    response = requests.get(url, headers= {
        'Authorization': f'Bearer {access_token}'
    })
    response.raise_for_status()
    anime_list = response.json()
    response.close()
    return anime_list

def get_animeinfo(access_token: str, anime_id: int) -> dict:
    """
    Returns a dictionary of the anime information
    """
    url = f'https://api.myanimelist.net/v2/anime/{anime_id}?fields=id,title,main_picture,alternative_titles,synopsis,mean,rank,popularity,num_list_users,media_type,status,genres,my_list_status,num_episodes,start_season,source,studios'
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
    user.animeentry_set.all().delete()
    animelist = get_animelist(access_token)['data']
    for i in animelist:
        # Query for anime ID and obtaining anime info
        # ------------------------------------------
        mal_id = i['node']['id']
        anime_info = get_animeinfo(access_token, mal_id)
        # Defining Intial Params
        # ----------------------
        #title
        title = anime_info['title']
        #status
        status = anime_info['my_list_status']['status']
        #teps
        t_eps = anime_info['num_episodes']
        #eps
        eps = 0
        if 'num_watched_episodes' in anime_info['my_list_status']:
            eps = anime_info['my_list_status']['num_watched_episodes']
        if status == 'completed':
            eps = t_eps
        score = anime_info['my_list_status']['score']
        #mean
        mean = 0
        if 'mean' in anime_info:
            mean = anime_info['mean']
        #picture
        picture = anime_info['main_picture']['medium']
        if 'large' in anime_info['main_picture']:
            picture = anime_info['main_picture']['large']
        #rewatching
        rewatching = anime_info['my_list_status']['is_rewatching']
        #desc
        desc = anime_info['synopsis']
        #rewatched
        rewatched = 0
        if 'num_times_rewatched' in anime_info['my_list_status']:
            rewatched = anime_info['my_list_status']['num_times_rewatched']
        #comments
        comments = ""
        if 'comments' in anime_info['my_list_status']:
            comments = anime_info['my_list_status']['comments']
        #prio
        prio = 0
        if 'priority' in anime_info['my_list_status']:
            prio = anime_info['my_list_status']['priority']
        #studio
        studio = ""
        if len(anime_info['studios']) > 0:
            studio = anime_info['studios'][0]['name']
        #airing_time
        airing_time = (anime_info['start_season']['season']).capitalize() + " " + str(anime_info['start_season']['year'])
        #anime status
        anime_status = anime_info['status']
        #source
        source = anime_info['source']
        #genres
        genres = anime_info['genres'][0]['name']
        #ranked
        ranked = 0
        if 'rank' in anime_info:
            ranked = anime_info['rank']
        #popularity
        popularity = anime_info['popularity']
        #members
        members = anime_info['num_list_users']
        #link
        link = f'https://myanimelist.net/anime/{mal_id}/{title}'
        #alt tile
        alt_title = ""
        if 'jp' in anime_info['alternative_titles']:
            alt_title = anime_info['alternative_titles']['jp']
        # Intialization of Anime Entry and Adding to User's Animelist
        # ----------------------------------------------------------
        anime_entry = AnimeEntry(mal_id = mal_id,
            title = title,
            eps = eps,
            status = status,
            score = score,
            mean = mean,
            picture = picture,
            rewatching = rewatching,
            rewatched = rewatched,
            comments = comments,
            prio = prio,
            studio = studio,
            airing_time = airing_time,
            anime_status = anime_status,
            source = source,
            genres = genres,
            ranked = ranked,
            popularity = popularity,
            members = members,
            link = link,
            alt_title = alt_title,
            t_eps = t_eps,
            userp = user,
            desc = desc
        )
        anime_entry.save()

