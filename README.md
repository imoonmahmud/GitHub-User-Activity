# GitHub User Activity CLI

A command-line tool that fetches and displays a GitHub user's recent public activity, using the GitHub Events API. No external libraries, built entirely with Python's standard library (`urllib`, `json`, `argparse`).

## Features

- Fetches a user's recent activity directly from the GitHub API
- Formats different event types into readable, human-friendly lines
- Limit how many events are shown with `-n`
- Graceful error handling for invalid usernames, rate limits, and network issues
- Zero dependencies — only Python's standard library

## Installation

```bash
git clone https://github.com/your-username/github-user-activity.git
cd github-user-activity
```

No `pip install` needed.

## Usage

```bash
python main.py <username>
```

### Examples

```bash
python main.py imoonmahmud
```
```
- Pushed to master in imoonmahmud/taskly
- Created repository in imoonmahmud/github-activity
- Starred psf/requests
```

Limit the number of events shown:
```bash
python main.py imoonmahmud -n 5
```

Invalid username:
```bash
python main.py some-fake-username-xyz123
```
```
Error: user 'some-fake-username-xyz123' not found.
```
## How it works

1. `fetch_events(username)` calls `https://api.github.com/users/<username>/events` using `urllib.request`.
2. The raw response bytes are decoded into text, then parsed into Python data with `json.loads()`.
3. `format_event(event)` looks at each event's `"type"` and builds a readable sentence from its `"repo"` and `"payload"` data.
4. `argparse` handles the command-line username argument and the optional `-n`/`--limit` flag.

## Project structure

```
github-user-activity/
├── main.py       # CLI entry point, dispatch, and formatting logic
├── request.py    # fetch_events() — talks to the GitHub API
└── README.md
```

## Lessons learned

- **`json.load()` vs `json.loads()`** — `load` reads directly from a file object (something with `.read()`), while `loads` parses a string you already have in memory. Mixing them up throws `AttributeError: 'str' object has no attribute 'read'`.
- **GitHub's API changes over time.** Push event payloads used to include a full list of commits; GitHub later removed that data to speed up the API. Code written against outdated documentation can silently stop matching reality — always be ready to adapt.
- **Unauthenticated API rate limits are easy to hit** (60 requests/hour per IP on GitHub). Wrapping requests in proper error handling (`403` for rate limits, `404` for missing users, `URLError` for connection issues) keeps the tool useful instead of crashing.
- **A fallback branch matters.** Rather than handling every possible GitHub event type, a generic `else` case means new or rare event types degrade gracefully instead of breaking the program.

## Acknowledgements

Project idea and requirements from roadmap.sh - [GitHub User Activity](https://roadmap.sh/projects/github-user-activity).
