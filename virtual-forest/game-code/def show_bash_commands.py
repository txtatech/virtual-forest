def show_bash_commands():
    bash_commands = """
Bash Commands:
|-- File Operations:
|   |-- ls          # List files and directories in the current directory
|   |-- cd          # Change the current directory
|   |-- pwd         # Print the current working directory
|   |-- touch       # Create an empty file
|   |-- mkdir       # Create a new directory
|   |-- rm          # Remove files or directories
|   |-- mv          # Move or rename files or directories
|   |-- cp          # Copy files or directories
|
|-- Text Processing:
|   |-- cat         # Concatenate and display file content
|   |-- grep        # Search for patterns in files
|   |-- sed         # Stream editor for text manipulation
|   |-- awk         # Pattern scanning and processing language
|
|-- File Content Viewing:
|   |-- head        # Display the beginning of a file
|   |-- tail        # Display the end of a file
|   |-- less        # View file content interactively
|
|-- File Permissions:
|   |-- chmod       # Change file permissions
|   |-- chown       # Change file owner
|   |-- chgrp       # Change file group
|
|-- Process Management:
|   |-- ps          # Display information about running processes
|   |-- top         # Monitor system processes in real-time
|   |-- kill        # Terminate processes
|
|-- System Information:
|   |-- uname       # Print system information
|   |-- df          # Display disk space usage
|   |-- free        # Display free and used memory
|
|-- Networking:
|   |-- ping        # Send ICMP ECHO_REQUEST packets to network hosts
|   |-- ifconfig    # Configure network interfaces
|   |-- ssh         # Secure shell remote login
|
|-- Miscellaneous:
|   |-- echo        # Print a message to the terminal
|   |-- date        # Display or set the system date and time
|   |-- history     # Display command history
|   |-- man         # Display manual page for commands
|
|-- Command Modifiers:
|   |-- >           # Redirect output to a file (overwrite)
|   |-- >>          # Redirect output to a file (append)
|   |-- <           # Redirect input from a file
|   |-- |           # Redirect output of one command to another (piping)
|   |-- &           # Run a command in the background
|   |-- ;           # Execute multiple commands sequentially
|   |-- &&          # Execute a command only if the previous one succeeds
|   |-- ||          # Execute a command only if the previous one fails
"""
    return bash_commands
