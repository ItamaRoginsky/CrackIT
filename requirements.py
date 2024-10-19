import subprocess
import sys
import zipfile
import os

# Path to the zip file and the destination directory
zip_file_path = 'rockyou.txt.7z'
destination_path = './'  # Current directory or specify a path

# Check if the zip file exists
if os.path.exists(zip_file_path):
    print(f"Unzipping {zip_file_path}...")
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(destination_path)
    print(f"Extraction complete. Files extracted to: {destination_path}")
else:
    print(f"{zip_file_path} not found!")

# List of required packages
required_packages = [
    "itertools",
    "random",
    "os",
    "time",
    "hashlib",
    "re"
]

def install(package):
    """Install a package using pip."""
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def main():
    """Main function to check and install required packages."""
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            print(f"{package} not found. Installing...")
            install(package)
        else:
            print(f"{package} is already installed.")

if __name__ == "__main__":
    main()
