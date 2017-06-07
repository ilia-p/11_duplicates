import os
from collections import defaultdict
import argparse

parser = argparse.ArgumentParser(description = 'Path_to_folder')
parser.add_argument('-p', '--path', type = str, required = True, help = 'Path to folder to explore')

def get_file_list(folder_to_explore):
    file_dict = defaultdict(list)
    for root, dirs, files in os.walk(folder_to_explore):
        for name in files:
            file_size = str(os.path.getsize(os.path.join(root,name)))
            file_name = (name, file_size)
            file_dict[file_name].append(root)
    return file_dict
    
def print_duplicates(file_dict):
    duplicates_list = [file for file in file_dict if len(file_dict[file]) > 1]
    for file in duplicates_list:
        file_name = file[0]
        file_size = file[1]
        print('file_name: ', file_name, ' |', ' size: ', file_size)

if __name__ == '__main__':
    arg = parser.parse_args()
    file_dict = get_file_list(arg.path)
    print_duplicates(file_dict)