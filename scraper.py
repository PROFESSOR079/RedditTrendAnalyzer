import time
from hn_client import get_top_story_ids, get_new_story_ids, get_best_story_ids, get_story_by_id

def fetch_stories(story_type="top", limit=50):
    if story_type == "top":
        ids = get_top_story_ids(limit)
    elif story_type == "new":
        ids = get_new_story_ids(limit)
    elif story_type == "best":
        ids = get_best_story_ids(limit)
    else:
        raise ValueError(f"Invalid story type: {story_type}")

    stories = []
    for story_id in ids:
        try:
            story = get_story_by_id(story_id)
            if story and story.get("type") == "story":
                stories.append({
                    "id": story.get("id"),
                    "title": story.get("title"),
                    "url": story.get("url", ""),
                    "score": story.get("score", 0),
                    "comments": story.get("descendants", 0),
                    "author": story.get("by", ""),
                    "time": story.get("time", 0),
                })
        except Exception:
            continue
        time.sleep(0.05)

    return stories