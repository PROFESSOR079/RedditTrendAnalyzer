from hn_client import test_connection
from scraper import fetch_stories
from analyzer import analyze_stories

if __name__ == "__main__":
    test_connection()
    stories = fetch_stories(story_type="top", limit=30)
    stats = analyze_stories(stories)
    print(f"Total: {stats['total_stories']}")
    print(f"Avg Score: {stats['avg_score']}")
    print(f"Peak Hour: {stats['peak_hour']}:00")