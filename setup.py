from setuptools import setup, find_packages

setup(
    name='ui_creator',
    version='0.0.1',
    description='An interactive application that leverages CrewAI’s multi-agent framework to generate and optimize simple UI python apps.',
    author='Erick Eduardo Ramirez Torres',
    author_email='erickeduardoramireztorres@gmail.com',
    packages=find_packages(),
    include_package_data=True,  # Ensure package data is included
    install_requires=[
        'streamlit==1.41.1',
        'crewai==0.105.0'
    ],
)

