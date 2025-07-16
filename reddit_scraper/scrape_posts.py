from .reddit_client import RedditClient

def get_user_name(url):
    # Extract username from URL, e.g. https://www.reddit.com/user/example_username/
    return url.rstrip('/').split('/')[-1]

class ScrapePosts:
    def __init__(self, url):
        self.user_name = get_user_name(url)
        try:
            self.client = RedditClient().client()
        except Exception as e:
            print(f"[ScrapePosts] Error initializing Reddit client: {e}")
            self.client = None
        self.posts_dict = {}

    def get_posts(self):
        if self.client is None:
            print("[ScrapePosts] Reddit client not available.")
            return {}
        try:
            redditor = self.client.redditor(self.user_name)
            for idx, submission in enumerate(redditor.submissions.new(limit=50), 1):
                try:
                    self.posts_dict[f"post_{idx}"] = {
                        "title": submission.title,
                        "selftext": submission.selftext,
                        "subreddit": str(submission.subreddit),
                        "created_utc": submission.created_utc,
                        "link": f"https://www.reddit.com{submission.permalink}"
                    }
                except Exception as e:
                    print(f"[ScrapePosts] Error parsing post {idx}: {e}")
            return self.posts_dict
        except Exception as e:
            print(f"[ScrapePosts] Error fetching posts for user '{self.user_name}': {e}")
            return {}
