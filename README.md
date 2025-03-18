# crew_ui_app_creator
An interactive application that leverages CrewAI multi-agent framework to generate and optimize simple UI python apps.

## Installation

1. **Clone the repository:**
    ```
    git clone https://github.com/eramireztorres/crew_ui_app_creator.git
    cd crew_ui_app_creator
    ```
    
2. **Set up a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. **Install the required packages:**
    Run the following command to install dependencies:
    ```bash
    pip install .
    ```
    
## Export the API keys of your models

### OpenAI Models

For OpenAI models, export your API key as an environment variable:

Linux or macOS:

```bash
export OPENAI_API_KEY='your_openai_api_key_here'
```

Or in windows:

```bash
setx OPENAI_API_KEY "your_openai_api_key_here"
```

You can export API keys for other model providers in a similar way by using the corresponding environment variable names:

- **Gemini**: Use GEMINI_API_KEY
- **Anthropic**: Use ANTHROPIC_API_KEY
- **OpenRouter**: Use OPENROUTER_API_KEY


## Launching the Web UI

Run the following command to launch the Streamlit app:

```bash
cd ui_creator
streamlit run app.py
```

This will open the application in your default web browser.


## License

This project is licensed under the MIT License.