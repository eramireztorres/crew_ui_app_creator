import streamlit as st
from ui_creator.crew.crew_manager import execute_crew
from ui_creator.utils.file_utils import txt_to_py
import os

def prepend_provider(model, provider):
    """
    Prepend the provider prefix to the model string if it's not already present.
    """
    if not model.startswith(provider + "/"):
        return f"{provider}/{model}"
    return model

# st.title("CrewAI Code Generator")

# st.sidebar.header("API Keys and Model Settings")
# openai_api_key = st.sidebar.text_input("OpenAI API Key")
# anthropic_api_key = st.sidebar.text_input("Anthropic API Key")
# gemini_api_key = st.sidebar.text_input("Gemini API Key")
# openrouter_api_key = st.sidebar.text_input("OpenRouter API Key")

def set_env_variable(key, value):
    os.environ[key] = value  # Sets in the current session (works across OS)

    # Persistent setting depending on OS
    if os.name == 'nt':  # Windows
        os.system(f'setx {key} "{value}"')
    else:  # Unix-based (Linux/Mac)
        bashrc_path = os.path.expanduser('~/.bashrc')
        with open(bashrc_path, 'a') as f:
            f.write(f'\nexport {key}="{value}"\n')


# Load existing environment variables if they exist
existing_openai_key = os.getenv("OPENAI_API_KEY", "")
existing_openrouter_key = os.getenv("OPENROUTER_API_KEY", "")
existing_gemini_key = os.getenv("GEMINI_API_KEY", "") 
existing_anthropic_key = os.getenv("ANTHROPIC_API_KEY", "")


st.set_page_config(
    page_title="CrewAI Code Generator",
    page_icon="💺",
    layout="wide"
)

st.sidebar.header("⚙️ API Key Settings")

# Input for OpenAI API Key (pre-populated if already set)
openai_api_key = st.sidebar.text_input(
    "Enter your OpenAI API Key:",
    value=existing_openai_key,
    type="password"
)


# New: Input for Gemini API Key (pre-populated if already set)
gemini_api_key = st.sidebar.text_input(
    "Enter your Gemini API Key:",
    value=existing_gemini_key,
    type="password"
)

# New: Input for Gemini API Key (pre-populated if already set)
anthropic_api_key = st.sidebar.text_input(
    "Enter your Anthropic API Key:",
    value=existing_anthropic_key,
    type="password"
)


# Input for OpenRouter API Key (pre-populated if already set)
openrouter_api_key = st.sidebar.text_input(
    "Enter your OpenRouter API Key:",
    value=existing_openrouter_key,
    type="password"
)


# Button to save API keys
if st.sidebar.button("Save API Keys"):
    if openai_api_key:
        set_env_variable("OPENAI_API_KEY", openai_api_key)
        st.sidebar.success("OpenAI API Key saved successfully!")
    if openrouter_api_key:
        set_env_variable("OPENROUTER_API_KEY", openrouter_api_key)
        st.sidebar.success("OpenRouter API Key saved successfully!")
    if gemini_api_key:
        set_env_variable("GEMINI_API_KEY", gemini_api_key)
        st.sidebar.success("Gemini API Key saved successfully!")
    if anthropic_api_key:
        set_env_variable("ANTHROPIC_API_KEY", anthropic_api_key)
        st.sidebar.success("Anthropic API Key saved successfully!")
    if not (openai_api_key or openrouter_api_key or gemini_api_key or anthropic_api_key):
        st.sidebar.warning("Please enter at least one API key to save.")

# st.sidebar.header("Application Settings")
app_description = st.sidebar.text_area("App Description")
ui_preference = st.sidebar.selectbox("UI Preference", ["CLI", "Tkinter", "Streamlit"])


def infer_provider(model_name: str) -> str:
    """
    Infer the provider from the model name using the following rules:
    1. If the model name contains '/', provider is "openrouter".
    2. If the model name contains "gpt", "o1", or "o3" (case-insensitive), provider is "openai".
    3. If the model name contains "gemini" or "gemma" (case-insensitive), provider is "gemini".
    4. If the model name contains "claude" (case-insensitive), provider is "anthropic".
    """
    if '/' in model_name:
        return "openrouter"
    model_lower = model_name.lower()
    if any(substr in model_lower for substr in ['gpt', 'o1', 'o3']):
        return "openai"
    if any(substr in model_lower for substr in ['gemini', 'gemma']):
        return "gemini"
    if 'claude' in model_lower:
        return "anthropic"
    return ""

st.sidebar.header("Agent Model & Provider Settings")

# Skeleton Generator
skeleton_generator_model = st.sidebar.text_input("Skeleton Generator Model", "gpt-4o-mini", key="skeleton_generator_model")
skeleton_generator_provider = infer_provider(skeleton_generator_model)
st.sidebar.text_input("Skeleton Generator Provider", value=skeleton_generator_provider, key="skeleton_generator_provider", disabled=True)

# Skeleton Reviewer
skeleton_reviewer_model = st.sidebar.text_input("Skeleton Reviewer Model", "gpt-4o-mini", key="skeleton_reviewer_model")
skeleton_reviewer_provider = infer_provider(skeleton_reviewer_model)
st.sidebar.text_input("Skeleton Reviewer Provider", value=skeleton_reviewer_provider, key="skeleton_reviewer_provider", disabled=True)

# UI Generator
ui_generator_model = st.sidebar.text_input("UI Generator Model", "gpt-4o-mini", key="ui_generator_model")
ui_generator_provider = infer_provider(ui_generator_model)
st.sidebar.text_input("UI Generator Provider", value=ui_generator_provider, key="ui_generator_provider", disabled=True)

# UI Reviewer
ui_reviewer_model = st.sidebar.text_input("UI Reviewer Model", "gpt-4o-mini", key="ui_reviewer_model")
ui_reviewer_provider = infer_provider(ui_reviewer_model)
st.sidebar.text_input("UI Reviewer Provider", value=ui_reviewer_provider, key="ui_reviewer_provider", disabled=True)


if st.button("Execute Crew"):
    # Prepend provider prefixes to the models
    skeleton_generator_model_full = prepend_provider(skeleton_generator_model, skeleton_generator_provider)
    skeleton_reviewer_model_full = prepend_provider(skeleton_reviewer_model, skeleton_reviewer_provider)
    ui_generator_model_full = prepend_provider(ui_generator_model, ui_generator_provider)
    ui_reviewer_model_full = prepend_provider(ui_reviewer_model, ui_reviewer_provider)
    
    user_inputs = {
        "app_description": app_description,
        "ui_preference": ui_preference,
        # Use the updated full model strings
        "skeleton_generator_model": skeleton_generator_model_full,
        "skeleton_generator_provider": skeleton_generator_provider,
        "skeleton_reviewer_model": skeleton_reviewer_model_full,
        "skeleton_reviewer_provider": skeleton_reviewer_provider,
        "ui_generator_model": ui_generator_model_full,
        "ui_generator_provider": ui_generator_provider,
        "ui_reviewer_model": ui_reviewer_model_full,
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
    
    # Create a ZIP archive for both files
    import zipfile, io
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zipf:
        for file in files_map.values():
            with open(file, "r", encoding="utf-8") as f:
                content = f.read()
            zipf.writestr(file.split('/')[-1], content)
    zip_buffer.seek(0)
    
    st.download_button(
        label="Download All Files as ZIP",
        data=zip_buffer,
        file_name="generated_code.zip",
        mime="application/zip"
    )
