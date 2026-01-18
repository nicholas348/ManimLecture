import subprocess

# Simple command (list files)
# shell=True is needed on Windows for built-in commands like 'dir'
# shell=False (default) is safer for security
result = subprocess.run(['ls', '-l'], capture_output=True, text=True)

print(f"Output:\n{result.stdout}")

try:
    # Attempting to ping a website
    # -c 4 means 4 packets (Linux/Mac). Use -n 4 on Windows.
    subprocess.run(['ping', '-c', '4', 'google.com'], check=True)
except subprocess.CalledProcessError as e:
    print(f"Command failed with error code {e.returncode}")