import os
from collections import defaultdict
import argparse

parser = argparse.ArgumentParser(description = 'Path_to_folder')
parser.add_argument('-p', '--path', type = str, required = True, help = 'Path to folder to explore')
arg = parser.parse_args()

def file_list(folder_to_explore):
    file_dict = defaultdict(list)
    for root, dirs, files in os.walk(folder_to_explore):
        for name in files:
            file_size = str(os.path.getsize(os.path.join(root,name)))
            file_name = (name, 'size = ' + file_size)
            file_dict[file_name].append(root)
    return file_dict
    
def duplicates(file_dict):
    duplicates_list = [item for item in file_dict if len(file_dict[item]) > 1]
    for item in duplicates_list:
        print(item)

if __name__ == '__main__':
    file_dict = file_list(arg.path)
    duplicates(file_dict)