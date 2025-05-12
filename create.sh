#!/bin/bash
#
# Create a git branch and directory with empty files.

DIR_NAME="$1"

# Check if a directory name was provided
if [ -z "$DIR_NAME" ]; then
  echo "Usage: $0 <directory_name>"
  exit 1
fi

# Add this block to check if the directory already exists
if [ -d "$DIR_NAME" ]; then
  echo "Error: Directory '$DIR_NAME' already exists. Please choose a different name."
  exit 1
fi

# Check if it's a Git repository
if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "Error: Not a Git repository. Please run this script inside a Git repository."
  exit 1
fi

# Create and checkout the Git branch
git checkout -b "$DIR_NAME"

# Create the directory
mkdir -p "$DIR_NAME"

# Create empty files under the directory
touch "$DIR_NAME/step1.py"
touch "$DIR_NAME/step2.py"
touch "$DIR_NAME/step3.py"
touch "$DIR_NAME/memo.md"

echo "Directory '$DIR_NAME' created with empty files: step1.py, step2.py, step3.py, memo.md"