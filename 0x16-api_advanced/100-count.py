#!/usr/bin/python3
"""
100-count
"""
import requests

def count_words(subreddit, word_list, after=None, counts=None):
    """Recursively queries the Reddit API and prints a sorted count of keywords in hot articles"""
    if counts is None:
        counts = {}
    if after is None:
        url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    else:
        url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit, after)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return
    data = response.json()
    for post in data['data']['children']:
        title = post['data']['title'].lower()
        for word in word_list:
            if ' ' + word.lower() + ' ' in title:
                if word.lower() in counts:
                    counts[word.lower()] += title.count(' ' + word.lower() + ' ')
                else:
                    counts[word.lower()] = title.count(' ' + word.lower() + ' ')
    if data['data']['after'] is not None:
        count_words(subreddit, word_list, after=data['data']['after'], counts=counts)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(word, count)
