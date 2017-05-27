import os
from collections import defaultdict

def duplicates(folder_to_explore):
    root_dict = defaultdict(list)
    for root, dirs, files in os.walk(folder_to_explore):
        for name in files:
            file_size = str(os.path.getsize(os.path.join(root,name)))
            file_uniq = name + ', size=' + file_size
            root_dict[file_uniq].append(root)
    for item in root_dict:
        if len(root_dict[item]) > 1:
            quantity = len(root_dict[item])
            print('\nФайл ', item, 'встречается ', quantity, ' раз(а) в папках:')
            for path in root_dict[item]:
                print(path)

if __name__ == '__main__':
    # pass
    folder_to_explore = input('Введите имя (путь до) папки\n')
    duplicates(folder_to_explore)