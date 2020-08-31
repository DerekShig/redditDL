import praw
import urllib.request
import requests
import os
import sys
from tqdm import tqdm
import argparse
from datetime import datetime

# program usage: py main.py [-u] [user/subreddit] [sort category] [# posts] ['directory']


def download(posts, num, folder):
    inter = False
    try:
        for submission in tqdm(posts, total=num):
            index = submission.rfind('/')
            url = submission[index + 1:]
            if submission.endswith('.gifv'):
                submission = submission.replace('.gifv', '.mp4')
                url = url.replace('.gifv', '.mp4')
            try:
                urllib.request.urlretrieve(submission, url)
            except:
                print('Malfunction downloading image. Process aborted.')
                inter = True
                sys.exit()
    except KeyboardInterrupt:
        print('Program terminated')
        sys.exit()
    except:
        if inter:
            sys.exit()
        os.chdir('..')
        os.rmdir(folder)


def create_folder(user, location, directory):
    try:
        os.chdir(directory)
    except OSError:
        print('Error in directory path. Default to current directory.')
    if user:
        path = str(datetime.today().strftime('%Y-%m-%d')) + ' user-' + str(location)
    else:
        path = str(datetime.today().strftime('%Y-%m-%d')) + ' subreddit-' + str(location)
    if not os.path.exists(path):
        os.mkdir(path)
        os.chdir(path)
    else:
        os.chdir(path)
    return path


def get_posts(reddit, user, location, category):
    if user:
        if category == 'hot':
            post = reddit.redditor(str(location)).submissions.hot(limit=1000)
        elif category == 'new':
            post = reddit.redditor(str(location)).submissions.new(limit=1000)
        else:
            post = reddit.redditor(str(location)).submissions.top(limit=1000)
    else:
        if category == 'hot':
            post = reddit.subreddit(str(location)).hot(limit=1000)
        elif category == 'new':
            post = reddit.subreddit(str(location)).new(limit=1000)
        else:
            post = reddit.subreddit(str(location)).top(limit=1000)
    return post

def validate(posts, num_posts):
    formats = ('.jpg', '.png', '.gif', '.gifv')
    sites = []
    cnt = 0
    try:
        for post in posts:
            if cnt == int(num_posts):
                break
            if post.url.endswith(formats):
                sites.append(post.url)
                cnt += 1
    except KeyboardInterrupt:
        print('Program Terminated')
        sys.exit()
    except:
        print('User/Subreddit does not exist')
        sys.exit()
    return sites

def main():
    owd = os.getcwd()
    parser = argparse.ArgumentParser(description='Download pics')
    parser.add_argument('-u', '--user', action='store_true', help='Indicates user profile')
    parser.add_argument('location', help='Download location')
    parser.add_argument('category', choices=['hot', 'new', 'top'], help='Sort category')
    parser.add_argument('posts', type=int, help='Number of posts to download')
    parser.add_argument('directory', nargs='?', default='.', help='Directory location')
    args = parser.parse_args()
    reddit = praw.Reddit('redditDL')
    posts = get_posts(reddit, args.user, args.location, args.category)
    valid_links = validate(posts, args.posts)
    folder = create_folder(args.user, args.location, args.directory)
    download(valid_links, args.posts, folder)
    os.chdir(owd)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Program terminated')
        quit()
