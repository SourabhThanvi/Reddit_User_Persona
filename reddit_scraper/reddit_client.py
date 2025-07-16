import praw
from praw.exceptions import APIException, ClientException
from dotenv import load_dotenv
import os

load_dotenv()

class RedditClient:
    '''
    RedditClient is a class that provides a client for the Reddit API.
    It is used to get the posts and comments from a user.
    '''
    def __init__(self):
        self.reddit_id = os.getenv('REDDIT_ID')
        self.reddit_secret = os.getenv('REDDIT_SECERT')
        self.user_agent = 'BeyondChats'
        # self.user_name = os.getenv('REDDIT_USERNAME')
        # self.password= os.getenv('REDDIT_PASSWORD')

    def client(self):
        try:
            reddit = praw.Reddit(
                client_id=self.reddit_id,
                client_secret=self.reddit_secret,
                user_agent=self.user_agent,
                # username = self.user_name,
                # password = self.password,
                # check_for_async=False
            )

            return reddit
        except (APIException, ClientException) as e:
            print(f"[RedditClient] PRAW error during client initialization: {e}")
            return None
        except Exception as e:
            print(f"[RedditClient] Unexpected error during client initialization: {e}")
            return None
