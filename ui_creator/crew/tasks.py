from crewai import Task

# Skeleton Code Generation Task (no output file)
skeleton_task = Task(
    description=(
        "Implement complete Python code for {app_description} with full docstrings and robust design."
    ),
    expected_output="A complete Python codebase for {app_description}.",
    agent=None,  # to be set by crew_manager using code_skeleton_generator
    verbose=True
)

# Skeleton Code Review Task (outputs to file)
skeleton_code_review_task = Task(
    description=(
        "Review the generated skeleton code. Optimize and ensure it fully meets {app_description} requirements. "
        "Identify any potential error sources—such as unhandled exceptions, missing error handling, or dependency issues—that could stop execution, "
        "and fix or handle them appropriately."
    ),
    expected_output="Optimized, robust Python code for {app_description} that includes proper error handling.",
    agent=None,  # to be set via python_code_reviewer in crew_manager
    output_file="skeleton_code.txt",
    verbose=True
)

# UI Code Generation Task (generic - will be replaced based on UI preference)
ui_task = Task(
    description=(
        "Develop a user interface using {ui_preference} for {app_description}."
    ),
    expected_output="UI code in {ui_preference} for {app_description}.",
    agent=None,  # to be assigned one of the specialized UI developers
    verbose=True
)

# UI Code Review Task (outputs to file)
ui_code_review_task = Task(
    description=(
        "Review the generated UI code. Optimize and ensure it fully meets {app_description} and adheres to {ui_preference} best practices. "
        "Identify any potential error sources—such as unhandled exceptions, incorrect event handling, or missing error checks—that could cause execution failures, "
        "and incorporate fixes or error handling measures as needed."
    ),
    expected_output="Optimized, robust UI code for {app_description} meeting {ui_preference} standards, with proper error handling.",
    agent=None,  # to be assigned one of the specialized UI code reviewers
    output_file="ui_code.txt",
    verbose=True
)
