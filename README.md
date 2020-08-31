# redditDL :camera:
Reddit script to download images.

## Installation

This script requires python 3+ to function. Modules used are [praw](https://github.com/praw-dev/praw) for reddit API and [tqdm](https://github.com/tqdm/tqdm).

```bash
pip install requirements.txt
```

To use the script you need to have a reddit account as well as a developer application set up. First login to your reddit account, then go [here](https://www.reddit.com/prefs/apps/). Click create app, give it a name and fill in the redirect uri with http://localhost:8080 or another of your choice. In praw.ini, 
fill in the client id, secret and user agent with your information (see [here](https://raw.githubusercontent.com/DerekShig/redditDL/master/setup.png)). The user agent is a short description of the bot that reddit can access. For example: "Python image downloader v2.0 (by /u/reddituser )".

## Usage

```bash
py main.py [-u] [-h] [location] [category] [posts] [directory]
```
| Option | Description |
| --- | --- |
| -h | Shows help text |
| -u | Denotes user reddit profile |
| location | User or subreddit location |
| category | Sort category for posts (hot, new, top) |
| posts | Number of posts to download |
| directory | Directory to download images to. If no directory provided, will default to cwd. If error in directory, defaults to cwd. Directory must be enclosed in single quotes|

**Example usage**
```bash
py main.py wallpapers top 20
py main.py -u spez new 50 'C:\Users\Derek\Documents'
```
