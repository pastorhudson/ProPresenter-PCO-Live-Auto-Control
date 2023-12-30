#!/bin/bash

# GitHub repository details
REPO_OWNER="pastorhudson"
REPO_NAME="ProPresenter-PCO-Live-Auto-Control"

# Get the directory where the script is located
SCRIPT_DIR="$(dirname "$0")"
EXTRACTED_DIR=""

# Define the virtual environment directory relative to the script location
VENV_DIR="./.venv"

# Check for the existing extracted directory
EXTRACTED_DIR=$(ls -dt ./"${REPO_OWNER}-${REPO_NAME}-"*/ | head -n 1)

if [ -z "$EXTRACTED_DIR" ]; then
    # Fetch the latest release tarball URL if no extracted directory exists
    LATEST_RELEASE_URL=$(curl -s "https://api.github.com/repos/${REPO_OWNER}/${REPO_NAME}/releases/latest" | grep tarball_url | cut -d '"' -f 4)

    # Check if the URL was successfully retrieved
    if [ -z "$LATEST_RELEASE_URL" ]; then
        echo "Failed to retrieve the latest release URL."
        exit 1
    fi

    echo "Latest release URL: $LATEST_RELEASE_URL"

    # Download and extract the latest release
    wget -O latest_release.tar.gz "$LATEST_RELEASE_URL"
    tar -xzf latest_release.tar.gz
    rm latest_release.tar.gz

    # Find the extracted directory again after extraction
    EXTRACTED_DIR=$(ls -dt ./"${REPO_OWNER}-${REPO_NAME}-"*/ | head -n 1)

    # Check if the extracted directory is found
    if [ -z "$EXTRACTED_DIR" ]; then
        echo "Failed to find the extracted directory."
        exit 1
    fi
fi

echo "Using directory: $EXTRACTED_DIR"

# Move into the extracted directory
cd "$EXTRACTED_DIR" || exit 1

# Check if the virtual environment directory exists
if [ ! -d "$VENV_DIR" ]; then
    echo "Virtual environment not found. Creating one now..."
    # Create the virtual environment
    python3 -m venv "$VENV_DIR"

    # Activate the virtual environment
    source "$VENV_DIR/bin/activate"

    # Install requirements
    pip install -r "./src/requirements.txt"
else
    echo "Activating existing virtual environment..."
    # Activate the virtual environment
    source "$VENV_DIR/bin/activate"
fi

# Pass all command-line arguments to the Python script
echo "Running Python script with arguments: $@"
python src/main.py "$@"

# Deactivate the virtual environment
deactivate
