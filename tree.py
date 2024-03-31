import os
import pyperclip

def display_filtered_directory_tree(startpath, output_file):
    ignore_dirs = ['venv', '__pycache__', 'DjangoBaseStartWithAuthTemplate']
    ignore_files = ['.DS_Store', 'db.sqlite3', 'tree.py', 'tree.txt']  # Add any other filenames you want to ignore to this list
    
    with open(output_file, 'w') as f:
        for root, dirs, files in os.walk(startpath):
            # Remove directories in the ignore list
            dirs[:] = [d for d in dirs if d not in ignore_dirs]
            
            # Remove files in the ignore list
            files = [file for file in files if file not in ignore_files]

            level = root.replace(startpath, '').count(os.sep)
            indent = ' ' * 4 * (level)
            f.write('{}{}/\n'.format(indent, os.path.basename(root)))

            subindent = ' ' * 4 * (level + 1)
            for file in files:
                if file.endswith('.py') or file.endswith('.txt'):
                    f.write('{}{}\n'.format(subindent, file))

    # Copy content of the file to clipboard
    with open(output_file, 'r') as f:
        content = f.read()
        pyperclip.copy(content)

    print(f"Directory tree has been saved to {output_file} and copied to clipboard.")

# Use the directory of the current script as the starting path
current_directory = os.path.dirname(os.path.abspath(__file__))
output_file = 'tree.txt'

display_filtered_directory_tree(current_directory, output_file)
