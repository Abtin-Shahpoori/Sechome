import sys
from extract import extract_files
from check import check_file

# TODO: add the feature bellow
DONT_SEARCH = []
files = extract_files(sys.argv[1])
pattern = sys.argv[2]
for file in files:
    if file in DONT_SEARCH:
        continue
    if check_file(file, rf"{pattern}") != None:
        data_arr = check_file(file, rf"{pattern}")
        for data in data_arr:
            print("on file" + data["file"].name + "\non line " + data["line"] + "\ncontent:\t" + data["content"])
            print("----------------------------------------------------------------------------")
