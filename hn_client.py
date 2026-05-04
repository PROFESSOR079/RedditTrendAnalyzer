import requests

BASE_URL = "https://hacker-news.firebaseio.com/v0"

def get_top_story_ids(limit=50):
    url = f"{BASE_URL}/topstories.json"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()[:limit]

def get_new_story_ids(limit=50):
    url = f"{BASE_URL}/newstories.json"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()[:limit]

def get_best_story_ids(limit=50):
    url = f"{BASE_URL}/beststories.json"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()[:limit]

def get_story_by_id(story_id):
    url = f"{BASE_URL}/item/{story_id}.json"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def test_connection():
    try:
        ids = get_top_story_ids(limit=1)
        if ids:
            print("✅ HackerNews API connection successful!")
            return True
    except requests.exceptions.RequestException as e:
        print(f"❌ Connection failed: {e}")
        return False