import strip_markdown
import os

class PersonaFileCreator:
    def __init__(self, output_dir=None):
        self.output_dir = output_dir or os.getcwd()

    def save_persona(self, persona_markdown, filename="persona_output.txt"):
        plain_text = strip_markdown.strip_markdown(persona_markdown)
        filepath = os.path.join(self.output_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(plain_text)
        return filepath
