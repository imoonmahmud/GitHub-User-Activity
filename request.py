import urllib.request
import json

def fetch_events(username):
    url = f"https://api.github.com/users/{username}/events"
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(url)
        return json.loads(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f'Error: user {username} not found.')
        elif e.code == 403:
            print('Error: GitHub API rate limit exceeded. Try again later.')
        else:
            print(f'Error: GitHub returned status {e.code}')
        return None
    except urllib.error.URLError as e:
        print(f'Error: could not reach GitHub ({e.code})')