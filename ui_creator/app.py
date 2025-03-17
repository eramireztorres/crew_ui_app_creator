import streamlit as st
from ui_creator.crew.crew_manager import execute_crew
from ui_creator.utils.file_utils import txt_to_py
import os

st.title("CrewAI Code Generator")

st.sidebar.header("API Keys and Model Settings")
openai_api_key = st.sidebar.text_input("OpenAI API Key")
anthropic_api_key = st.sidebar.text_input("Anthropic API Key")
gemini_api_key = st.sidebar.text_input("Gemini API Key")
openrouter_api_key = st.sidebar.text_input("OpenRouter API Key")

st.sidebar.header("Application Settings")
app_description = st.sidebar.text_area("App Description")
ui_preference = st.sidebar.selectbox("UI Preference", ["CLI", "Tkinter", "Streamlit"])

st.sidebar.header("Agent Model & Provider Settings")
skeleton_generator_model = st.sidebar.text_input("Skeleton Generator Model", "openai/gpt-4o-mini")
skeleton_generator_provider = st.sidebar.text_input("Skeleton Generator Provider", "openai")
skeleton_reviewer_model = st.sidebar.text_input("Skeleton Reviewer Model", "openai/gpt-4o-mini")
skeleton_reviewer_provider = st.sidebar.text_input("Skeleton Reviewer Provider", "openai")
ui_generator_model = st.sidebar.text_input("UI Generator Model", "openai/gpt-4o-mini")
ui_generator_provider = st.sidebar.text_input("UI Generator Provider", "openai")
ui_reviewer_model = st.sidebar.text_input("UI Reviewer Model", "openai/gpt-4o-mini")
ui_reviewer_provider = st.sidebar.text_input("UI Reviewer Provider", "openai")

if st.button("Execute Crew"):
    user_inputs = {
        "app_description": app_description,
        "ui_preference": ui_preference,
        # Additional keys for model/provider settings can be passed here
        "skeleton_generator_model": skeleton_generator_model,
        "skeleton_generator_provider": skeleton_generator_provider,
        "skeleton_reviewer_model": skeleton_reviewer_model,
        "skeleton_reviewer_provider": skeleton_reviewer_provider,
        "ui_generator_model": ui_generator_model,
        "ui_generator_provider": ui_generator_provider,
        "ui_reviewer_model": ui_reviewer_model,
        "ui_reviewer_provider": ui_reviewer_provider
    }
    st.info("Executing crew, please wait...")
    result = execute_crew(user_inputs)
    # Convert output .txt files to .py files
    files_map = {
        "skeleton_code.txt": "outputs/skeleton_code.py",
        "ui_code.txt": "outputs/ui_code.py"
    }
    txt_to_py(files_map)
    st.success("Crew execution finished!")
    # Provide download links
    for file in files_map.values():
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
        st.download_button(label=f"Download {file.split('/')[-1]}", data=content, file_name=file.split('/')[-1])
