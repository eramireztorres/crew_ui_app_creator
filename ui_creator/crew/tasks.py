from crewai import Task

# --- Core Logic (Skeleton) Tasks ---

# Task to generate the core business logic code
skeleton_task = Task(
    description=(
        "Implement the complete Python code for {app_description} that includes all the necessary core logic "
        "(such as classes, functions, and algorithms) required to perform the application's operations. "
        "This output must contain only the core business logic and must NOT include any user interface (UI) code. "
        "Focus exclusively on data processing, algorithms, and business rules."
    ),
    expected_output="A complete Python module for {app_description} that contains only the core logic (no UI code).",
    agent=None,  # to be set by crew_manager using code_skeleton_generator
    verbose=True
)

# Task to review and optimize the core logic
skeleton_code_review_task = Task(
    description=(
        "Review and optimize the core logic code generated. "
        "Ensure that it fully meets {app_description} requirements and contains no UI-related code. "
        "Remove any inadvertent UI components and add robust error handling and documentation as needed."
    ),
    expected_output="Optimized, robust core logic module for {app_description} with proper error handling and documentation, without any UI code.",
    agent=None,  # to be set via python_code_reviewer in crew_manager
    output_file="skeleton_code.txt",
    verbose=True
)

# --- UI Tasks ---

# Task to generate the UI code that interacts with the core logic
ui_task = Task(
    description=(
        "Develop the user interface code using {ui_preference} for {app_description}. "
        "The UI code must be entirely separate from business logic. It should contain only UI-related code "
        "that handles user input, layout, and event handling. Critically, it must include a mandatory import statement "
        "at the top that imports all the necessary classes and functions from the provided core code as in 'skeleton_code' script module (e.g., 'from skeleton_code import ...'). "
        "Do not duplicate any logic from the provided core code."
    ),
    expected_output="A Python module containing only UI code for {app_description} that adheres to {ui_preference} best practices and includes an import statement from skeleton_code.",
    agent=None,  # to be assigned one of the specialized UI developers
    verbose=True
)

# Task to review and optimize the UI code
ui_code_review_task = Task(
    description=(
        "Review the generated UI code. Optimize it so that it adheres to {ui_preference} best practices. "
        "Ensure that the UI code does not duplicate any business logic from the core module. It must contain a mandatory import statement, "
        "for example: 'from skeleton_code import <required elements>', to access the core logic. Remove any redundant code and add appropriate error handling."
    ),
    expected_output="Optimized, robust UI module for {app_description} that follows {ui_preference} standards, includes the required import from skeleton_code, and contains no duplicated core logic.",
    agent=None,  # to be assigned one of the specialized UI code reviewers
    output_file="ui_code.txt",
    verbose=True
)


# from crewai import Task

# # Updated Skeleton Code Generation Task (core logic only, no UI)
# skeleton_task = Task(
#     description=(
#         "Implement complete Python code for {app_description} that includes all the core logic "
#         "(classes, functions, and algorithms required to perform the necessary tasks) but explicitly excludes any UI-related code. "
#         "Focus solely on business logic and data processing."
#     ),
#     expected_output="A complete Python codebase for {app_description} containing only the core logic (no UI code).",
#     agent=None,  # to be set by crew_manager using code_skeleton_generator
#     verbose=True
# )

# # Updated Skeleton Code Review Task (ensure no UI code is included)
# skeleton_code_review_task = Task(
#     description=(
#         "Review and optimize the generated skeleton code from the previous task. Ensure it fully meets {app_description} requirements, "
#         "includes robust error handling, and contains only the core logic. There must be no UI-related code in this output."
#     ),
#     expected_output="Optimized, robust core logic code for {app_description} with proper error handling and without any UI code.",
#     agent=None,  # to be set via python_code_reviewer in crew_manager
#     output_file="skeleton_code.txt",
#     verbose=True
# )

# # Updated UI Code Generation Task (UI-only; must import core logic)
# ui_task = Task(
#     description=(
#         "Develop a user interface using {ui_preference} for {app_description} that interacts with the core logic. "
#         "The UI code must not contain any business logic but should instead import the necessary classes and functions from the 'skeleton_code' module. "
#         "Ensure that the code includes a mandatory import statement (e.g., 'from skeleton_code import ...')."
#     ),
#     expected_output="UI code in {ui_preference} for {app_description} that exclusively handles the user interface and includes an import from skeleton_code.",
#     agent=None,  # to be assigned one of the specialized UI developers
#     verbose=True
# )

# # Updated UI Code Review Task (verify UI code does not duplicate core logic)
# ui_code_review_task = Task(
#     description=(
#         "Review the generated UI code. Optimize it to ensure that it fully meets {app_description} requirements and adheres to {ui_preference} best practices. "
#         "Critically, the UI code must not duplicate any core logic; it must include a mandatory import statement (e.g., 'from skeleton_code import ...') "
#         "to access the business logic. Identify and fix any potential error sources, such as unhandled exceptions or incorrect event handling."
#     ),
#     expected_output="Optimized, robust UI code for {app_description} that meets {ui_preference} standards, includes the required import from skeleton_code, and does not duplicate any core logic.",
#     agent=None,  # to be assigned one of the specialized UI code reviewers
#     output_file="ui_code.txt",
#     verbose=True
# )


