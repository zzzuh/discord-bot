from xmlrpc.server import CGIXMLRPCRequestHandler
import praw
import secret
from pymongo import MongoClient

def reddit_scraper():
    reddit = praw.Reddit(client_id = secret.ID, client_secret = secret.SECRET, user_agent = "Scraper 1.0 by zzzuh")
    subreddit = reddit.subreddit("buildapcsales")

    cluster = MongoClient(secret.MONGO_URL)
    db = cluster["buildAPC"]
    my_collection = db['pcParts']


    for post in subreddit.stream.submissions():
        flair = post.link_flair_text
        title = post.title
        url = post.url

        if "Expired" in flair:
            continue

        if my_collection.count_documents({'Title': title}, limit = 1) != 0:
            continue

        submission = {"Category": flair, "Title": title, "Link": url}
        my_collection.insert_one(submission)
        print(title, flair, url)
        

def main():
    reddit_scraper()

if __name__ == "__main__":
    main()



