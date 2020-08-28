# redditDL :camera:
Reddit script to download images.

## Installation

This script requires python 3+ to function. Modules used are [praw](https://github.com/praw-dev/praw) for reddit API and [tqdm](https://github.com/tqdm/tqdm).

```bash
pip install requirements.txt
```
## Usage

```bash
py main.py [-u] [-h] [location] [category] [posts] [directory]
```
-h: Shows help text
-u: Denotes user reddit profile
location: User or subreddit location
category: Sort category for posts (hot, new, top)
posts: Number of posts to download
directory: Directory to download images to. If no directory provided, will default to cwd. If error in directory, defaults to cwd.

| Command | Description |
| --- | --- |
| git status | List all new or modified files |
| git diff | Show file differences that haven't been staged |
