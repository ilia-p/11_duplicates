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
            file_id = (name, file_size)
            file_dict[file_id].append(root)
    return file_dict
    
def print_duplicates(file_dict):
    duplicates_dict = dict([(file, file_dict[file]) for file in file_dict if len(file_dict[file]) > 1])
    for file_id, paths in duplicates_dict.items():
        print('\nfile: {0}\nsize: {1}'.format(file_id[0], file_id[1]))
        print('\n'.join(path for path in paths))

if __name__ == '__main__':
    arg = parser.parse_args()
    file_dict = get_file_list(arg.path)
    print_duplicates(file_dict)