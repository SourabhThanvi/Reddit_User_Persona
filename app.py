# app.py

import streamlit as st
from llm_engine.llm_invoke import GeminiInvocation
from llm_engine.persona_writer import PersonaFileCreator

st.title("Reddit User Persona Generator")

url = st.text_input("Enter Reddit Profile URL")

if st.button("Generate Persona"):
    with st.spinner("Generating persona..."):
        persona_markdown = GeminiInvocation(url).invocation()
        if persona_markdown:
            writer = PersonaFileCreator()
            file_path = writer.save_persona(persona_markdown)
            st.success("Persona generated!")
            with open(file_path, "r", encoding="utf-8") as f:
                persona_text = f.read()
            st.text_area("Persona (plain text)", persona_text, height=400)
            st.download_button("Download Persona", data=persona_text, file_name="persona.txt")
        else:
            st.error("Failed to generate persona.")
