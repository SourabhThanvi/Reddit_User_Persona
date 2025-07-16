from .llm_init import GeminiClient
from prompts import comment_prompt, persona_prompt, post_prompt, system_prompt
from reddit_scraper import scrape_comments, scrape_posts

class GeminiInvocation:
    def __init__(self, URL):
        # Scrape data with error handling
        try:
            self.comment_dict = scrape_comments.ScrapeComments(URL).get_comments()
        except Exception as e:
            print(f"[ERROR] Failed to fetch comments: {e}")
            self.comment_dict = {}

        try:
            self.post_dict = scrape_posts.ScrapePosts(URL).get_posts()
        except Exception as e:
            print(f"[ERROR] Failed to fetch posts: {e}")
            self.post_dict = {}

        # Initialize prompt templates
        self.system_prompt = system_prompt.SystemPrompt().get_prompt()
        self.comment_prompt = comment_prompt.CommentPrompt().get_prompt(self.comment_dict)
        self.post_prompt = post_prompt.PostPrompt().get_prompt(self.post_dict)

        # Initialize Gemini client
        try:
            self.client = GeminiClient().get_client()
        except Exception as e:
            print(f"[ERROR] Gemini client initialization failed: {e}")
            self.client = None

    def invocation(self):
        if not self.client:
            print("[ERROR] No Gemini client available.")
            return None
        try:
            # Generate post response
            response_post = self.client.generate_content(self.post_prompt)
            post_text = response_post.text if hasattr(response_post, 'text') else str(response_post)

            # Generate comment response
            response_comment = self.client.generate_content(self.comment_prompt)
            comment_text = response_comment.text if hasattr(response_comment, 'text') else str(response_comment)

            # Use both post and comment LLM outputs to construct the persona prompt
            persona_prompt_text = persona_prompt.PersonaPrompt().get_prompt(post_text, comment_text)

            # Generate persona
            response_persona = self.client.generate_content(persona_prompt_text)
            return response_persona.text if hasattr(response_persona, 'text') else str(response_persona)
        except Exception as e:
            print(f"[ERROR] LLM invocation failed: {e}")
            return None
