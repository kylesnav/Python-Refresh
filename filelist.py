import os
from pathlib import Path

def get_files_and_folders(path):
    entries = os.listdir(path)
    files = []
    folders = []

    for entry in entries:
        full_path = os.path.join(path, entry)
        if os.path.isfile(full_path):
            files.append(entry)
        elif os.path.isdir(full_path):
            folders.append(entry)

    return files, folders

def write_tree_entry(entry, depth, file):
    indentation = '  ' * depth
    file.write(f'{indentation}{entry}\n')
    print(indentation + entry)

def create_tree(path, file, depth=0):
    files, folders = get_files_and_folders(path)
    
    for folder in folders:
        write_tree_entry(folder, depth, file)
        create_tree(os.path.join(path, folder), file, depth + 1)

    for file_name in files:
        write_tree_entry(file_name, depth, file)

def main():
    start_path = os.path.expanduser("~")
    tree_file_path = os.path.join(os.path.expanduser("~"), "Desktop", "file_tree.txt")

    with open(tree_file_path, "w") as tree_file:
        create_tree(start_path, tree_file)

if __name__ == '__main__':
    main()