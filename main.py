from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from llm_engine.llm_invoke import GeminiInvocation
from llm_engine.persona_writer import PersonaFileCreator

app = FastAPI()

class UserProfileRequest(BaseModel):
    reddit_url: str

@app.post("/generate-persona/")
def generate_persona(req: UserProfileRequest):
    persona_markdown = GeminiInvocation(req.reddit_url).invocation()
    if not persona_markdown:
        raise HTTPException(status_code=400, detail="Failed to generate persona.")
    # Save file and return content or download link
    writer = PersonaFileCreator()
    file_path = writer.save_persona(persona_markdown, filename="persona_output.txt")
    # Optionally: return the text, or a URL to download the file
    return {"persona_text": open(file_path, encoding="utf-8").read()}

# To run: uvicorn main:app --reload
