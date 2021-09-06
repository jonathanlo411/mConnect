from django.shortcuts import render
import requests

# Page Renders
def animelist(request):
    name = grab_name(tk)
    context = {
        "name": name
    }
    return render(request, 'animelist/animelist.html', context)



# Helper Functions
def grab_name(access_token: str):
    """
    Grabs the user's MAL name
    """
    url = 'https://api.myanimelist.net/v2/users/@me'
    response = requests.get(url, headers = {
        'Authorization': f'Bearer {access_token}'
        })
    response.raise_for_status()
    user = response.json()
    response.close()
    return user['name']