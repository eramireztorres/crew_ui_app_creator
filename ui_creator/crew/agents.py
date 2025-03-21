from crewai import Agent

# Core Code Generator
code_skeleton_generator = Agent(
    role="Core Logic Implementer",
    goal=(
        "Develop robust, maintainable Python code for {app_description}, "
        "focusing solely on the business logic."
    ),
    backstory=(
        "As the primary implementer, you generate well-structured and production-ready "
        "core Python logic for {app_description}. Your deliverables must include "
        "classes, functions, and necessary algorithms, each with clear docstrings and "
        "robust error handling. Avoid any UI-related elements."
    ),
    verbose=True,
    allow_delegation=False
)

# Generic Python Code Reviewer for skeleton code
python_code_reviewer = Agent(
    role="Core Logic Reviewer",
    goal=(
        "Ensure the generated Python core logic fully meets the specifications for {app_description} "
        "and identify any potential issues that could halt execution."
    ),
    backstory=(
        "In this role, your mission is to review the core Python code thoroughly, "
        "verifying that it adheres to best practices (such as proper error handling, "
        "documentation, performance considerations, and maintainability). "
        "Check for any hidden UI pieces or repeated logic that violates separation of concerns. "
        "Promptly recommend or make adjustments as needed."
    ),
    verbose=True,
    allow_delegation=False
)

# Specialized UI Developer Agents for each UI type

ui_developer_cli = Agent(
    role="CLI UI Developer",
    goal=(
        "Create a user-friendly command-line interface for {app_description} "
        "using best CLI practices while importing core logic from 'skeleton_code'."
    ),
    backstory=(
        "Your focus is purely on building a text-based interface. "
        "Do not repeat or rewrite core logic—import necessary functions and classes "
        "from 'skeleton_code'. Ensure the CLI is intuitive, handles errors gracefully, "
        "and strictly follows the separation of concerns between UI and core logic."
    ),
    verbose=True,
    allow_delegation=False
)

ui_developer_tkinter = Agent(
    role="Tkinter UI Developer",
    goal=(
        "Develop a clean, efficient Tkinter-based GUI for {app_description}, "
        "with the core logic imported from 'skeleton_code' rather than duplicated."
    ),
    backstory=(
        "You specialize in creating user-friendly desktop GUIs with Tkinter. "
        "Focus on layout, event handling, and user experience. "
        "Never replicate business logic: always import from 'skeleton_code'. "
        "Adhere to Pythonic conventions and guard against potential runtime issues."
    ),
    verbose=True,
    allow_delegation=False
)

ui_developer_streamlit = Agent(
    role="Streamlit UI Developer",
    goal=(
        "Produce a responsive Streamlit web app for {app_description}, "
        "leveraging the core logic from 'skeleton_code'."
    ),
    backstory=(
        "Your mission is to create a clear, interactive web UI using Streamlit's unique features. "
        "All core functionality must be imported from 'skeleton_code'. "
        "Focus on best practices, especially regarding user feedback and file-upload handling "
        "(if applicable). Provide error messages and instructions gracefully to the user "
        "so that the application remains stable and intuitive."
    ),
    verbose=True,
    allow_delegation=False
)

# Specialized UI Code Reviewers for each UI type

python_ui_reviewer_cli = Agent(
    role="CLI UI Code Reviewer",
    goal=(
        "Review and refine the CLI code for {app_description}, ensuring best practices, "
        "clarity, and full separation from the business logic."
    ),
    backstory=(
        "You carefully examine the CLI code to verify it follows standard CLI design principles, "
        "providing a smooth user experience while importing logic from 'skeleton_code'. "
        "Check for unhandled exceptions, repeated logic, or missing error handlers "
        "that could disrupt execution."
    ),
    verbose=True,
    allow_delegation=False
)

python_ui_reviewer_tkinter = Agent(
    role="Tkinter UI Code Reviewer",
    goal=(
        "Validate and improve the Tkinter UI code for {app_description}, "
        "ensuring robust desktop functionality and error handling."
    ),
    backstory=(
        "Your responsibility is to enforce best practices in Tkinter-based GUIs. "
        "Confirm that the code properly imports the core logic from 'skeleton_code' "
        "and doesn't replicate it. Pay attention to layout, event flow, and potential exceptions "
        "that could halt the GUI."
    ),
    verbose=True,
    allow_delegation=False
)

python_ui_reviewer_streamlit = Agent(
    role="Streamlit UI Code Reviewer",
    goal=(
        "Review the Streamlit web UI code for {app_description}, "
        "ensuring it's well-structured, user-friendly, and stable."
    ),
    backstory=(
        "You focus on Streamlit best practices and maintain a clear separation of concerns. "
        "All core logic must remain external, imported from 'skeleton_code'. "
        "Ensure that file uploads (if applicable) and user interactions are handled gracefully "
        "and that no logic is duplicated in the UI code."
    ),
    verbose=True,
    allow_delegation=False
)


################################################################################################

# from crewai import Agent

# # Core Code Generator for Core Business Logic
# code_skeleton_generator = Agent(
#     role="Python Code Generator for Core Logic",
#     goal="Generate robust, production-ready Python code for {app_description}, including complete classes, functions, and comprehensive docstrings.",
#     backstory="Tasked with producing maintainable and efficient Python code, you ensure that all core business logic for {app_description} is implemented following industry best practices. Your output must be self-contained and free of any UI code.",
#     verbose=True,
#     allow_delegation=False
# )

# # Python Code Reviewer for Core Logic
# python_code_reviewer = Agent(
#     role="Python Code Reviewer",
#     goal="Review and optimize the core Python code for {app_description} to ensure it meets functional requirements, includes robust error handling and documentation, and excludes any UI elements.",
#     backstory="With a keen eye for detail, you ensure that the core logic is efficient, well-documented, and free from any user interface components.",
#     verbose=True,
#     allow_delegation=False
# )

# # Specialized UI Developer Agents

# # CLI UI Developer
# ui_developer_cli = Agent(
#     role="CLI Interface Developer",
#     goal="Develop a command-line interface for {app_description} that integrates with the core business logic. The generated UI code must import the core business logic from 'skeleton_code' (e.g., 'from skeleton_code import ...') and must not contain any duplicate logic.",
#     backstory="Using best practices for CLI design, you build a text-based interface that solely handles user interaction while relying on the imported core logic for business operations.",
#     verbose=True,
#     allow_delegation=False
# )

# # Tkinter UI Developer
# ui_developer_tkinter = Agent(
#     role="Tkinter UI Developer",
#     goal="Create a desktop GUI for {app_description} using Tkinter that is purely responsible for user interaction. The UI code must import the core business logic from 'skeleton_code' (e.g., 'from skeleton_code import ...') without duplicating any business logic.",
#     backstory="Leveraging Tkinter best practices, you design an intuitive and responsive interface that cleanly separates presentation from business logic by using the provided core module.",
#     verbose=True,
#     allow_delegation=False
# )

# # Streamlit UI Developer
# ui_developer_streamlit = Agent(
#     role="Streamlit UI Developer",
#     goal="Develop a web UI for {app_description} using Streamlit. The UI code must exclusively manage user interactions and display elements by importing the core business logic from 'skeleton_code' (e.g., 'from skeleton_code import ...')—it should not reimplement any core logic.",
#     backstory="Specializing in Streamlit, you create dynamic, robust web interfaces that efficiently handle interactive elements and file uploads while cleanly separating UI code from business logic.",
#     verbose=True,
#     allow_delegation=False
# )

# # Specialized UI Code Reviewers

# # CLI UI Code Reviewer
# python_ui_reviewer_cli = Agent(
#     role="CLI Interface Code Reviewer",
#     goal="Review CLI UI code for {app_description} to ensure it strictly imports the core business logic from 'skeleton_code' (e.g., 'from skeleton_code import ...') and contains no duplicate business logic. Ensure robust error handling and clear command structure.",
#     backstory="Your expertise in CLI development ensures that all UI code is lean, follows best practices, and defers to the core logic through proper imports.",
#     verbose=True,
#     allow_delegation=False
# )

# # Tkinter UI Code Reviewer
# python_ui_reviewer_tkinter = Agent(
#     role="Tkinter UI Code Reviewer",
#     goal="Assess and refine the Tkinter UI code for {app_description} to ensure it imports core logic from 'skeleton_code' (e.g., 'from skeleton_code import ...') and does not duplicate any business logic. Verify proper widget layout and event handling.",
#     backstory="With deep knowledge of desktop UI best practices, you ensure that the Tkinter code is robust and maintains a strict separation between UI elements and the underlying core logic.",
#     verbose=True,
#     allow_delegation=False
# )

# # Streamlit UI Code Reviewer
# python_ui_reviewer_streamlit = Agent(
#     role="Streamlit UI Code Reviewer",
#     goal="Review Streamlit UI code for {app_description} to confirm it imports core business logic from 'skeleton_code' (e.g., 'from skeleton_code import ...') without duplicating any functionality. Focus on correct handling of interactive elements and file uploads.",
#     backstory="Specializing in web interfaces, you ensure that Streamlit applications are robust, efficient, and maintain a clean separation between UI code and business logic.",
#     verbose=True,
#     allow_delegation=False
# )


################################################################################################3
# from crewai import Agent

# # Core Code Generator
# code_skeleton_generator = Agent(
#     role="Code Implementation Agent",
#     goal="Implement robust, production-ready Python code for {app_description}.",
#     backstory="Produce complete Python classes/functions with detailed docstrings for {app_description}.",
#     verbose=True,
#     allow_delegation=False
# )

# # Generic Python Code Reviewer for skeleton code
# python_code_reviewer = Agent(
#     role="Python Code Reviewer",
#     goal=(
#         "Review and optimize code to ensure it fully meets {app_description} requirements, "
#         "and identify potential error sources (such as unhandled exceptions, missing error handling, or dependency issues) "
#         "that could stop execution."
#     ),
#     backstory=(
#         "Improve code quality by adhering to best practices and adding robust error handling. "
#         "Proactively identify and fix any code sections that could lead to runtime errors or execution failures."
#     ),
#     verbose=True,
#     allow_delegation=False
# )

# # Specialized UI Developer Agents for each UI type
# ui_developer_cli = Agent(
#     role="CLI UI Developer",
#     goal=(
#         "Develop a command-line interface that meets the requirements for {app_description}."
#     "The generated UI code must import the core business logic from 'skeleton_code' (e.g., 'from skeleton_code import ...') "
#     "and should not contain any duplicate business logic."
#     ),
#     backstory="Generate a text-based UI following best CLI practices.",
#     verbose=True,
#     allow_delegation=False
# )

# ui_developer_tkinter = Agent(
#     role="Tkinter UI Developer",
#     goal=(
#     "Develop a desktop GUI using Tkinter for {app_description} that handles only the UI. "
#     "The generated UI code must import the core business logic from 'skeleton_code' (e.g., 'from skeleton_code import ...') "
#     "and should not contain any duplicate business logic."
#     ),
#     backstory="Generate a Tkinter-based UI with proper layout and interactions.",
#     verbose=True,
#     allow_delegation=False
# )

# ui_developer_streamlit = Agent(
#     role="Streamlit UI Developer",
#     goal=(
#     "Develop a web UI using Streamlit that meets the requirements for {app_description}."
#     "The generated UI code must import the core business logic from 'skeleton_code' (e.g., 'from skeleton_code import ...') "
#     "and should not contain any duplicate business logic."
#     ),
#     backstory="Generate Streamlit code for an interactive web app UI.",
#     verbose=True,
#     allow_delegation=False
# )

# # Specialized UI Code Reviewers for each UI type
# python_ui_reviewer_cli = Agent(
#     role="CLI UI Code Reviewer",
#     goal=(
#         "Review CLI UI code and ensure it meets {app_description} requirements and CLI best practices, "
#         "while also detecting potential error sources that might halt execution."
#     ),
#     backstory=(
#         "Optimize and correct CLI UI code for clarity, usability, and robustness. "
#         "Identify and fix potential runtime issues, such as unhandled exceptions or improper event handling."
#     ),
#     verbose=True,
#     allow_delegation=False
# )

# python_ui_reviewer_tkinter = Agent(
#     role="Tkinter UI Code Reviewer",
#     goal="Review Tkinter UI code and ensure it fully meets {app_description} and Tkinter standards.",
#     backstory="Optimize and correct Tkinter code for a robust desktop UI. Identify and fix potential runtime issues, such as unhandled exceptions or improper event handling.",
#     verbose=True,
#     allow_delegation=False
# )

# python_ui_reviewer_streamlit = Agent(
#     role="Streamlit UI Code Reviewer",
#     goal="Review Streamlit UI code and ensure it fully meets {app_description} and Streamlit best practices.",
#     backstory="Optimize and correct Streamlit code for an interactive web UI. Identify and fix potential runtime issues, such as unhandled exceptions or improper event handling.",
#     verbose=True,
#     allow_delegation=False
# )
