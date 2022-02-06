import re

def check_file(file_path, pattern):
    output_array = []
    file = open(file_path, "r", encoding='ISO-8859-1')
    for count,line in enumerate(file):
        if re.search(pattern, line):
            output_array.append(
                { 
                    "line": str(count + 1), 
                    "file": file, 
                    "content": line.strip() 
                }
            )
    file.close()
    return output_array or None
