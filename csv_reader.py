import csv
import os
import json
from os import listdir, path

def file_list(in_path):
    try:
        files = [f for f in listdir(in_path)]
        file_length = len(files)
        filename = []
        folder_list = []
        file_path = []
        sig_type = None

        for i in range(file_length):
            filename.append(0)

        for i in range(file_length):
            filename.append(files[i])
            abs_path = in_path + '\\' + str(files[i])
            folder_check = os.path.isdir(abs_path)
            if folder_check is True:
                folder_list.append(abs_path)

            file_path.append(os.path.abspath(os.path.join(abs_path, os.pardir)) + '\\'+ files[i])

        for i in range(0, len(folder_list)):
            file_list(folder_list[i])

        return file_path
    except:
        print("[Error] Path is not found. Check your input")

path = 'path'

for i in range(0, 1000):
    with open(file_list(path)[i], 'r') as f:
        reader = csv.reader(f)
        print('['+str(i)+']' + '' + str(file_list(path)[i].split('\\')[9]))
        # for txt in reader:
        #     print(txt)
        # print('===================================')




