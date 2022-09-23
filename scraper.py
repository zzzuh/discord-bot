from http import client
from telnetlib import SE
from turtle import pos, title
from unicodedata import name
import praw
import secret
import pandas as pd

# load_dotenv("/Users/zejun/Desktop/python projects/discord-bot/credentials.env")
# secret = os.getenv('SECRET')
# id = os.getenv("ID")
# print(secret)


def redditScraper():
    reddit = praw.Reddit(client_id = secret.ID, client_secret = secret.SECRET, user_agent = "Scraper 1.0 by zzzuh")
    subreddit = reddit.subreddit("buildapcsales")
    submissions = set()

    df = pd.DataFrame(columns = ["Title", "URL", "Category", "Price"])
    
    for post in subreddit.stream.submissions():
        flair = post.link_flair_text
        title = post.title
        price = ""
        url = post.url
        if "$" in title:
            price = title[title.index("$"):]
        print(pd.concat([df, pd.DataFrame({"Title": [title], "URL": [url], "Category": [flair], "Price": [price]})]))
        

def main():
    redditScraper()

if __name__ == "__main__":
    main()


redditScraper()



