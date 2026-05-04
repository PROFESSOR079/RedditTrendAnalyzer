from datetime import datetime

def analyze_stories(stories):
    if not stories:
        return {}

    scores = [s["score"] for s in stories]
    comments = [s["comments"] for s in stories]

    top_by_score = sorted(stories, key=lambda x: x["score"], reverse=True)[:5]
    top_by_comments = sorted(stories, key=lambda x: x["comments"], reverse=True)[:5]

    authors = {}
    for story in stories:
        author = story["author"]
        authors[author] = authors.get(author, 0) + 1
    most_active_authors = sorted(authors.items(), key=lambda x: x[1], reverse=True)[:5]

    hours = {}
    for story in stories:
        hour = datetime.fromtimestamp(story["time"]).hour
        hours[hour] = hours.get(hour, 0) + 1
    peak_hour = max(hours, key=hours.get)

    return {
        "total_stories": len(stories),
        "avg_score": round(sum(scores) / len(scores), 2),
        "max_score": max(scores),
        "min_score": min(scores),
        "avg_comments": round(sum(comments) / len(comments), 2),
        "top_by_score": top_by_score,
        "top_by_comments": top_by_comments,
        "most_active_authors": most_active_authors,
        "peak_hour": peak_hour,
    }