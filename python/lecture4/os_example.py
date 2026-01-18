import os

# 1. Get the current working directory
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

# 2. List files in a directory
files = os.listdir('.')
print(f"Files: {files}")

# 3. Create a new directory
if not os.path.exists("test_folder"):
    os.makedirs("test_folder")

# 4. Join paths (cross-platform compatible)
path = os.path.join(current_dir, "test_folder", "example.txt")
print(f"Formatted path: {path}")

# 5. Get environment variables
path_env = os.environ.get('PATH')