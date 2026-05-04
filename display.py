from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def print_stats(stats):
    panel = Panel(
        f"Total: {stats['total_stories']}  |  "
        f"Avg Score: {stats['avg_score']}  |  "
        f"Max Score: {stats['max_score']}  |  "
        f"Peak Hour: {stats['peak_hour']}:00",
        title="📊 HackerNews Stats",
        border_style="cyan"
    )
    console.print(panel)

def print_top_stories(stories):
    table = Table(title="🏆 Top Stories by Score", border_style="bright_yellow")
    table.add_column("Score", style="green", justify="right")
    table.add_column("Comments", style="blue", justify="right")
    table.add_column("Author", style="magenta")
    table.add_column("Title", style="white")

    for s in stories:
        table.add_row(
            str(s["score"]),
            str(s["comments"]),
            s["author"],
            s["title"][:70]
        )
    console.print(table)

def print_active_authors(authors):
    table = Table(title="✍️ Most Active Authors", border_style="bright_blue")
    table.add_column("Author", style="magenta")
    table.add_column("Posts", style="green", justify="right")

    for author, count in authors:
        table.add_row(author, str(count))
    console.print(table)