import os

def extract_files(root_dir):
    files_path = []
    for roots,dirs,files in os.walk(root_dir):
        for file in files:
            if file[0] == '.':
                continue
            else:
                files_path.append(roots + '/' + file)

    return files_path
