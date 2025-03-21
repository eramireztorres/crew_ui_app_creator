from crewai import Agent

# Core Code Generator
code_skeleton_generator = Agent(
    role="Code Implementation Agent",
    goal="Implement robust, production-ready Python code for {app_description}.",
    backstory="Produce complete Python classes/functions with detailed docstrings for {app_description}.",
    verbose=True,
    allow_delegation=False
)

# Generic Python Code Reviewer for skeleton code
python_code_reviewer = Agent(
    role="Python Code Reviewer",
    goal=(
        "Review and optimize code to ensure it fully meets {app_description} requirements, "
        "and identify potential error sources (such as unhandled exceptions, missing error handling, or dependency issues) "
        "that could stop execution."
    ),
    backstory=(
        "Improve code quality by adhering to best practices and adding robust error handling. "
        "Proactively identify and fix any code sections that could lead to runtime errors or execution failures."
    ),
    verbose=True,
    allow_delegation=False
)

# Specialized UI Developer Agents for each UI type
ui_developer_cli = Agent(
    role="CLI UI Developer",
    goal=(
        "Develop a command-line interface that meets the requirements for {app_description}."
    "The generated UI code must import the core business logic from 'skeleton_code' (e.g., 'from skeleton_code import ...') "
    "and should not contain any duplicate business logic."
    ),
    backstory="Generate a text-based UI following best CLI practices.",
    verbose=True,
    allow_delegation=False
)

ui_developer_tkinter = Agent(
    role="Tkinter UI Developer",
    goal=(
    "Develop a desktop GUI using Tkinter for {app_description} that handles only the UI. "
    "The generated UI code must import the core business logic from 'skeleton_code' (e.g., 'from skeleton_code import ...') "
    "and should not contain any duplicate business logic."
    ),
    backstory="Generate a Tkinter-based UI with proper layout and interactions.",
    verbose=True,
    allow_delegation=False
)

ui_developer_streamlit = Agent(
    role="Streamlit UI Developer",
    goal=(
    "Develop a web UI using Streamlit that meets the requirements for {app_description}."
    "The generated UI code must import the core business logic from 'skeleton_code' (e.g., 'from skeleton_code import ...') "
    "and should not contain any duplicate business logic."
    ),
    backstory="Generate Streamlit code for an interactive web app UI.",
    verbose=True,
    allow_delegation=False
)

# Specialized UI Code Reviewers for each UI type
python_ui_reviewer_cli = Agent(
    role="CLI UI Code Reviewer",
    goal=(
        "Review CLI UI code and ensure it meets {app_description} requirements and CLI best practices, "
        "while also detecting potential error sources that might halt execution."
    ),
    backstory=(
        "Optimize and correct CLI UI code for clarity, usability, and robustness. "
        "Identify and fix potential runtime issues, such as unhandled exceptions or improper event handling."
    ),
    verbose=True,
    allow_delegation=False
)

python_ui_reviewer_tkinter = Agent(
    role="Tkinter UI Code Reviewer",
    goal="Review Tkinter UI code and ensure it fully meets {app_description} and Tkinter standards.",
    backstory="Optimize and correct Tkinter code for a robust desktop UI. Identify and fix potential runtime issues, such as unhandled exceptions or improper event handling.",
    verbose=True,
    allow_delegation=False
)

python_ui_reviewer_streamlit = Agent(
    role="Streamlit UI Code Reviewer",
    goal="Review Streamlit UI code and ensure it fully meets {app_description} and Streamlit best practices.",
    backstory="Optimize and correct Streamlit code for an interactive web UI. Identify and fix potential runtime issues, such as unhandled exceptions or improper event handling.",
    verbose=True,
    allow_delegation=False
)
