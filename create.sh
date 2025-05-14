#!/bin/bash
#
# Create a git branch and directory with empty files, taking a title and a URL.
# Example usage:
# ./create.sh "82. Remove Duplicates from Sorted List II" https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/

# Convert a string to snake case
to_snake_case() {
  local s="$1"
  # Convert to lowercase, replace non-alphanumeric characters (except underscore) with underscores
  s=$(echo "$s" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/_/g')
  # Replace multiple underscores with a single underscore
  s=$(echo "$s" | sed 's/__*/_/g')
  # Remove leading/trailing underscores
  s=$(echo "$s" | sed 's/^_//;s/_$//')
  echo "$s"
}

TITLE="$1"
URL="$2"

# Check if a directory name was provided
if [ -z "$TITLE" ]; then
  echo "Usage: $0 <directory_name>"
  exit 1
fi

# Convert the raw input to snake case
DIR_NAME=$(to_snake_case "$TITLE")

# Check if it's a Git repository
if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "Error: Not a Git repository. Please run this script inside a Git repository."
  exit 1
fi

# Create and checkout the Git branch (always branch from main)
git checkout main
git checkout -b "$DIR_NAME"

# Create the directory
mkdir -p "$DIR_NAME"

# Create empty files under the directory
touch "$DIR_NAME/step1.py"
touch "$DIR_NAME/step2.py"
touch "$DIR_NAME/step3.py"
touch "$DIR_NAME/memo.md"

# Populate memo.md using a heredoc
cat << EOF > "$DIR_NAME/memo.md"
# $TITLE

$URL

## Comments

### step1

*

### step2

*

### step3

* 
EOF

echo "Directory '$DIR_NAME' created with template files: step1.py, step2.py, step3.py, memo.md"