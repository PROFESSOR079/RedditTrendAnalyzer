from hn_client import test_connection
from scraper import fetch_stories

if __name__ == "__main__":
    test_connection()
    stories = fetch_stories(story_type="top", limit=10)
    for story in stories:
        print(story["title"], "|", story["score"])