import argparse
from hn_client import test_connection
from scraper import fetch_stories
from analyzer import analyze_stories
from exporter import export_to_csv

def parse_args():
    parser = argparse.ArgumentParser(description="HackerNews Trend Analyzer")
    parser.add_argument("--type", choices=["top", "new", "best"], default="top", help="Story type to fetch")
    parser.add_argument("--limit", type=int, default=30, help="Number of stories to fetch")
    parser.add_argument("--export", action="store_true", help="Export results to CSV")
    return parser.parse_args()

def main():
    args = parse_args()

    print(f"\n🔍 Fetching {args.limit} {args.type} stories from HackerNews...\n")

    if not test_connection():
        return

    stories = fetch_stories(story_type=args.type, limit=args.limit)
    stats = analyze_stories(stories)

    print(f"Total Stories : {stats['total_stories']}")
    print(f"Avg Score     : {stats['avg_score']}")
    print(f"Max Score     : {stats['max_score']}")
    print(f"Avg Comments  : {stats['avg_comments']}")
    print(f"Peak Hour     : {stats['peak_hour']}:00")

    print("\n🏆 Top 5 by Score:")
    for s in stats["top_by_score"]:
        print(f"  {s['score']:>5} pts | {s['title'][:60]}")

    if args.export:
        export_to_csv(stories)

if __name__ == "__main__":
    main()