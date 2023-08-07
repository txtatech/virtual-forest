import os
import subprocess

def deploy_gofer_server():
    """
    deploy_gofer_server function deploys a Gofer server and serves the young AI's story to it.

    Returns:
        str: A message indicating the status of the deployment.
    """
    # Define the story file path (assumes the young AI has generated a story in a file)
    story_file = "/path/to/young_ai_story.txt"

    # Define the port number for the Gofer server
    gofer_port = 8000

    # Check if the story file exists
    if not os.path.exists(story_file):
        return "Error: The young AI's story file does not exist. Please generate a story first."

    # Deploy Gofer server using Python's built-in http.server module
    try:
        command = f"python -m http.server {gofer_port}"
        subprocess.Popen(command, shell=True, cwd=os.path.dirname(story_file))
        return f"Gofer server deployed! You can access the young AI's story at http://localhost:{gofer_port}"
    except Exception as e:
        return f"Error: Failed to deploy Gofer server. {str(e)}"
