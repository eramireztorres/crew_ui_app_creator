from crewai import Task

# Updated Skeleton Code Generation Task (core logic only, no UI)
skeleton_task = Task(
    description=(
        "Implement complete Python code for {app_description} that includes all the core logic "
        "(classes, functions, and algorithms required to perform the necessary tasks) but explicitly excludes any UI-related code. "
        "Focus solely on business logic and data processing."
    ),
    expected_output="A complete Python codebase for {app_description} containing only the core logic (no UI code).",
    agent=None,  # to be set by crew_manager using code_skeleton_generator
    verbose=True
)

# Updated Skeleton Code Review Task (ensure no UI code is included)
skeleton_code_review_task = Task(
    description=(
        "Review and optimize the generated skeleton code from the previous task. Ensure it fully meets {app_description} requirements, "
        "includes robust error handling, and contains only the core logic. There must be no UI-related code in this output."
    ),
    expected_output="Optimized, robust core logic code for {app_description} with proper error handling and without any UI code.",
    agent=None,  # to be set via python_code_reviewer in crew_manager
    output_file="skeleton_code.txt",
    verbose=True
)

# Updated UI Code Generation Task (UI-only; must import core logic)
ui_task = Task(
    description=(
        "Develop a user interface using {ui_preference} for {app_description} that interacts with the core logic. "
        "The UI code must not contain any business logic but should instead import the necessary classes and functions from the 'skeleton_code' module. "
        "Ensure that the code includes a mandatory import statement (e.g., 'from skeleton_code import ...')."
    ),
    expected_output="UI code in {ui_preference} for {app_description} that exclusively handles the user interface and includes an import from skeleton_code.",
    agent=None,  # to be assigned one of the specialized UI developers
    verbose=True
)

# Updated UI Code Review Task (verify UI code does not duplicate core logic)
ui_code_review_task = Task(
    description=(
        "Review the generated UI code. Optimize it to ensure that it fully meets {app_description} requirements and adheres to {ui_preference} best practices. "
        "Critically, the UI code must not duplicate any core logic; it must include a mandatory import statement (e.g., 'from skeleton_code import ...') "
        "to access the business logic. Identify and fix any potential error sources, such as unhandled exceptions or incorrect event handling."
    ),
    expected_output="Optimized, robust UI code for {app_description} that meets {ui_preference} standards, includes the required import from skeleton_code, and does not duplicate any core logic.",
    agent=None,  # to be assigned one of the specialized UI code reviewers
    output_file="ui_code.txt",
    verbose=True
)



# from crewai import Task

# # Skeleton Code Generation Task (no output file)
# skeleton_task = Task(
#     description=(
#         "Implement complete Python code for {app_description} with full docstrings and robust design."
#     ),
#     expected_output="A complete Python codebase for {app_description}.",
#     agent=None,  # to be set by crew_manager using code_skeleton_generator
#     verbose=True
# )

# # Skeleton Code Review Task (outputs to file)
# skeleton_code_review_task = Task(
#     description=(
#         "Review the generated skeleton code. Optimize and ensure it fully meets {app_description} requirements. "
#         "Identify any potential error sources—such as unhandled exceptions, missing error handling, or dependency issues—that could stop execution, "
#         "and fix or handle them appropriately."
#     ),
#     expected_output="Optimized, robust Python code for {app_description} that includes proper error handling.",
#     agent=None,  # to be set via python_code_reviewer in crew_manager
#     output_file="skeleton_code.txt",
#     verbose=True
# )

# # UI Code Generation Task (generic - will be replaced based on UI preference)
# ui_task = Task(
#     description=(
#         "Develop a user interface using {ui_preference} for {app_description}."
#     ),
#     expected_output="UI code in {ui_preference} for {app_description}.",
#     agent=None,  # to be assigned one of the specialized UI developers
#     verbose=True
# )

# # UI Code Review Task (outputs to file)
# ui_code_review_task = Task(
#     description=(
#         "Review the generated UI code. Optimize and ensure it fully meets {app_description} and adheres to {ui_preference} best practices. "
#         "Identify any potential error sources—such as unhandled exceptions, incorrect event handling, or missing error checks—that could cause execution failures, "
#         "and incorporate fixes or error handling measures as needed."
#     ),
#     expected_output="Optimized, robust UI code for {app_description} meeting {ui_preference} standards, with proper error handling.",
#     agent=None,  # to be assigned one of the specialized UI code reviewers
#     output_file="ui_code.txt",
#     verbose=True
# )
