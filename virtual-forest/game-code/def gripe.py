import subprocess

def gripe(pattern, filename):
    """
    gripe function demonstrates the usage of 'grep' to search for a pattern in a file.

    Args:
        pattern (str): The pattern to search for.
        filename (str): The name of the file to search in.

    Returns:
        str: The output of 'grep' command containing the matched lines.
    """
    try:
        # Run the 'grep' command using subprocess
        result = subprocess.run(['grep', pattern, filename], capture_output=True, text=True)
        if result.returncode == 0:
            # 'grep' command was successful
            return result.stdout
        else:
            # 'grep' command returned a non-zero exit code (indicating an error)
            return f"grep command failed with error: {result.stderr}"
    except Exception as e:
        return f"An error occurred while running grep: {str(e)}"

# Example usage:
pattern_to_search = "example"
filename_to_search = "sample.txt"
print(gripe(pattern_to_search, filename_to_search))