# HackerNews Trend Analyzer 📊

A Python CLI tool that fetches and analyzes trending stories from HackerNews
using the official HN Firebase API. No API key required.

## Features
- 🔍 Fetch top, new & best stories
- 📈 Analyze scores, comments, authors and peak posting hours
- 💾 Export data to CSV
- 🎨 Beautiful terminal output with Rich

## Tech Stack
- `requests` — API calls
- `pandas` — Data analysis
- `rich` — Terminal formatting

## Installation
```bash
git clone https://github.com/yourusername/hackernews-trend-analyzer
cd hackernews-trend-analyzer
pip install -r requirements.txt
```

## Usage
```bash
python main.py --type top --limit 30
python main.py --type best --limit 50 --export
python main.py --type new --limit 20
```

## Project Structure
```
├── hn_client.py   — API connection
├── scraper.py     — Story fetching
├── analyzer.py    — Data analysis
├── exporter.py    — CSV export
├── display.py     — Rich UI
└── main.py        — CLI entrypoint
```