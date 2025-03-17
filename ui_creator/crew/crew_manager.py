from ui_creator.crew import tasks
from crewai import Crew
from ui_creator.crew.agents import code_skeleton_generator, python_code_reviewer
from ui_creator.crew.agents import ui_developer_cli, ui_developer_tkinter, ui_developer_streamlit
from ui_creator.crew.agents import python_ui_reviewer_cli, python_ui_reviewer_tkinter, python_ui_reviewer_streamlit

def build_crew(user_inputs):
    """
    Build and return a Crew based on user inputs.
    user_inputs should include:
      - app_description, ui_preference
      - For each agent: model and provider settings (if needed)
    """
    ui_pref = user_inputs.get("ui_preference").lower()  # expected values: 'cli', 'tkinter', 'streamlit'
    
    # Assign UI developer and reviewer based on preference
    if ui_pref == "cli":
        ui_dev = ui_developer_cli
        ui_rev = python_ui_reviewer_cli
    elif ui_pref == "tkinter":
        ui_dev = ui_developer_tkinter
        ui_rev = python_ui_reviewer_tkinter
    elif ui_pref == "streamlit":
        ui_dev = ui_developer_streamlit
        ui_rev = python_ui_reviewer_streamlit
    else:
        raise ValueError("Invalid UI preference selected.")
    
    # Set agents for tasks
    tasks.skeleton_task.agent = code_skeleton_generator
    tasks.skeleton_code_review_task.agent = python_code_reviewer
    tasks.ui_task.agent = ui_dev
    tasks.ui_code_review_task.agent = ui_rev

    # Build the crew with these tasks (order matters)
    crew = Crew(
        agents=[
            code_skeleton_generator,
            ui_dev,
            python_code_reviewer,
            ui_rev
        ],
        tasks=[
            tasks.skeleton_task,
            tasks.skeleton_code_review_task,
            tasks.ui_task,
            tasks.ui_code_review_task
        ],
        verbose=True
    )
    return crew

def execute_crew(user_inputs):
    crew = build_crew(user_inputs)
    result = crew.kickoff(inputs=user_inputs)
    return result
