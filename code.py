import praw

reddit = praw.Reddit(
    client_id="my client id",
    client_secret="my client secret",
    password="my password",
    user_agent="my user agent", #Example: "Youtube Marketing by/u/my_username"
    username="my username",
)

subreddits = {'videos','youtube','subcscribe','youtubeviews','youtubevideos'}

#title of your post
title = "My First NFT Youtube Video"

#url of your youtube video
link = ""

for subreddit in subreddits:
    reddit.subreddit(subreddit).submit(title,url=link,send_replies=False)