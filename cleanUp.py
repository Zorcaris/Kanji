import re

# List of files to process
files_to_clean = [
    "build\\kanjiWindow\\Analysis-00.toc",
    "build\\kanjiWindow\\EXE-00.toc",
    "build\\kanjiWindow\\PKG-00.toc",
    "build\\kanjiWindow\\PYZ-00.toc",
    "build\\kanjiWindow\\xref-kanjiWindow.html"
]

# Define a regular expression to match absolute paths (this pattern assumes paths start with a drive letter and colon, such as "C:/")
absolute_path_pattern = re.compile(r"[A-Za-z]:[\\|/][^\n]+")  # This pattern matches paths like C:\path\to\file or C:/path/to/file

# Function to clean files by removing absolute paths
def clean_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Replace absolute paths with a placeholder (or empty string if you want to remove them entirely)
    cleaned_content = re.sub(absolute_path_pattern, "[REMOVED_PATH]", content)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(cleaned_content)

    print(f"Cleaned file: {file_path}")

# Iterate over the files and clean them
for file in files_to_clean:
    clean_file(file)
