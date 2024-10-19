import subprocess
import sys
import gzip
import shutil
import os

# Define the path to the Gzip file and the destination directory for extraction
file_path = 'rockyou.txt.gz'  # Path to the .gz file
destination_path = './'  # Destination directory; defaults to the current directory

# Check if the specified Gzip file exists
if os.path.exists(file_path):
    print(f"Extracting {file_path}...")
    # Open the Gzip file for reading in binary mode
    with gzip.open(file_path, 'rb') as f_in:
        # Open the destination file for writing in binary mode
        with open(os.path.join(destination_path, 'rockyou.txt'), 'wb') as f_out:
            # Copy the decompressed data from the Gzip file to the destination file
            shutil.copyfileobj(f_in, f_out)
    print(f"Extraction complete. Files extracted to: {destination_path}")
else:
    print(f"Error: {file_path} not found!")

# List of required packages for the project
required_packages = [
    "itertools",
    "random",
    "os",
    "time",
    "hashlib",
    "re"
]

def install(package):
    """Install a specified package using pip.

    Args:
        package (str): The name of the package to install.
    """
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def main():
    """Main function to check for and install required packages.

    This function iterates over the list of required packages, checking if each
    package is already installed. If a package is not found, it installs the package
    using pip.
    """
    for package in required_packages:
        try:
            # Attempt to import the package
            __import__(package)
        except ImportError:
            # If the package is not installed, install it
            print(f"{package} not found. Installing...")
            install(package)
        else:
            # Confirm the package is already installed
            print(f"{package} is already installed.")

if __name__ == "__main__":
    # Execute the main function
    main()
