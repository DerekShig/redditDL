import praw
import urllib.request
import os
import sys
from tqdm import tqdm
import argparse
from datetime import datetime

# program usage: py main.py [-u] [user/subreddit] [sort category] [# posts] ['directory']


def download(posts, num, user, folder):
    inter = False
    counter = 0
    try:
        for submission in tqdm(posts, total=num):
            if not submission.stickied:
                if submission.url.endswith('.jpg') or submission.url.endswith('.png'):
                    index = submission.url.rfind('/')
                    url = submission.url[index + 1:]
                    try:
                        urllib.request.urlretrieve(submission.url, url)
                    except:
                        print('Malfunction downloading image. Process aborted.')
                        print('Specified ' + str(num) + ' posts, ' + str(counter) + ' downloaded.')
                        inter = True
                        sys.exit()
                    else:
                        counter += 1
        print('Specified ' + str(num) + ' posts, ' + str(counter) + ' downloaded.')
    except:
        if inter:
            sys.exit()
        else:
            if user:
                print('User does not exist')
            else:
                print('Subreddit does not exist')
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


def get_posts(reddit, user, location, category, posts):
    if user:
        if category == 'hot':
            post = reddit.redditor(str(location)).submissions.hot(limit=int(posts))
        elif category == 'new':
            post = reddit.redditor(str(location)).submissions.new(limit=int(posts))
        else:
            post = reddit.redditor(str(location)).submissions.top(limit=int(posts))
    else:
        if category == 'hot':
            post = reddit.subreddit(str(location)).hot(limit=int(posts))
        elif category == 'new':
            post = reddit.subreddit(str(location)).new(limit=int(posts))
        else:
            post = reddit.subreddit(str(location)).top(limit=int(posts))
    return post


def main():
    owd = os.getcwd()
    parser = argparse.ArgumentParser(description='Download pics')
    parser.add_argument('-u', '--user', action='store_true', help='Indicates user profile')
    parser.add_argument('location', help='Download location')
    parser.add_argument('category', choices=['hot', 'new', 'top'], help='Sort category')
    parser.add_argument('posts', type=int, help='Number of posts to download')
    parser.add_argument('directory', nargs='?', default='.', help='Directory location')
    args = parser.parse_args()
    reddit = praw.Reddit(client_id='jGtoIPjsL-AlXQ',
                         client_secret='20W5ifxF7ZWSyPEIFxdaZZbUWH4',
                         user_agent='pc:jGtoIPjsL-AlXQ:0.1 (by /u/killer_catzilla')
    posts = get_posts(reddit, args.user, args.location, args.category, args.posts)
    folder = create_folder(args.user, args.location, args.directory)
    download(posts, args.posts, args.user, folder)
    os.chdir(owd)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Program terminated')
        quit()
