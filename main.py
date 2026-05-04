import argparse
from hn_client import test_connection
from scraper import fetch_stories
from analyzer import analyze_stories
from exporter import export_to_csv
from display import console, print_stats, print_top_stories, print_active_authors

def parse_args():
    parser = argparse.ArgumentParser(description="HackerNews Trend Analyzer")
    parser.add_argument("--type", choices=["top", "new", "best"], default="top")
    parser.add_argument("--limit", type=int, default=30)
    parser.add_argument("--export", action="store_true")
    return parser.parse_args()

def main():
    args = parse_args()

    console.print(f"\n[cyan]🔍 Fetching {args.limit} {args.type} stories...[/cyan]\n")

    if not test_connection():
        return

    stories = fetch_stories(story_type=args.type, limit=args.limit)
    stats = analyze_stories(stories)

    print_stats(stats)
    print_top_stories(stats["top_by_score"])
    print_active_authors(stats["most_active_authors"])

    if args.export:
        export_to_csv(stories)

if __name__ == "__main__":
    main()