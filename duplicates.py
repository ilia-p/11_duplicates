import os
from collections import defaultdict
import argparse

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
    # for item in file_dict:
    #     if len(file_dict[item]) > 1:
    #         quantity = len(file_dict[item])
    #         print('\nФайл ', item, 'встречается ', quantity, ' раз(а) в папках:')
    #         for path in file_dict[item]:
    #             print(path)

if __name__ == '__main__':
    # pass
    folder_to_explore = input('Введите имя (путь до) папки\n')
    file_dict = file_list(folder_to_explore)
    duplicates(file_dict)