import sys

# Print command line arguments (e.g., python script.py arg1 arg2)
print(f"Arguments passed: {sys.argv}")

# Check Python version
if sys.version_info < (3, 10):
    print("Warning: This script requires Python 3.10+")


import os

# Get current directory
current_dir = os.getcwd()
print(f"I am running in: {current_dir}")

# Check if a file exists safely
if os.path.exists("config.json"):
    print("Config file found.")
os.mkdir("Users/projects")


from pathlib import Path

# Create a path object
p = Path("data/2025/logs")

# parents=True: creates missing parents (like os.makedirs)
# exist_ok=True: ignores the error if the folder is already there
p.mkdir(parents=True, exist_ok=True)