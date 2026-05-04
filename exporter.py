import csv
import os
from datetime import datetime

def export_to_csv(stories, filename=None):
    if not stories:
        print("No stories to export.")
        return

    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"hn_stories_{timestamp}.csv"

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=stories[0].keys())
        writer.writeheader()
        writer.writerows(stories)

    print(f"Exported {len(stories)} stories to {filename}")
    return filename