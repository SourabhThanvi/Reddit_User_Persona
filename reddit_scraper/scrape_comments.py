from .reddit_client import RedditClient 

def get_user_name(url):
    # Extract username from URL, e.g. https://www.reddit.com/user/example_username/
    return url.rstrip('/').split('/')[-1]

class ScrapeComments:
    def __init__(self, url):
        self.user_name = get_user_name(url)
        try:
            self.client = RedditClient().client()
        except Exception as e:
            print(f"[ScrapeComments] Error initializing Reddit client: {e}")
            self.client = None
        self.comments_dict = {}

    def get_comments(self):
        if self.client is None:
            print("[ScrapeComments] Reddit client not available.")
            return {}
        try:
            redditor = self.client.redditor(self.user_name)
            for idx, comment in enumerate(redditor.comments.new(limit=50), 1):
                try:
                    self.comments_dict[f"comment_{idx}"] = {
                        "body": comment.body,
                        "subreddit": str(comment.subreddit),
                        "created_utc": comment.created_utc,
                        "link": f"https://www.reddit.com{comment.permalink}"
                    }
                except Exception as e:
                    print(f"[ScrapeComments] Error parsing comment {idx}: {e}")
            return self.comments_dict
        except Exception as e:
            print(f"[ScrapeComments] Error fetching comments for user '{self.user_name}': {e}")
            return {}
