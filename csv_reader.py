import csv
import os
import json
import pandas as pd
from os import listdir

def file_list(in_path):
    try:
        files = [f for f in listdir(in_path)]
        file_length = len(files)
        filename = []
        folder_list = []
        file_path = []

        for i in range(file_length):
            filename.append(0)

        for i in range(file_length):
            filename.append(files[i])
            abs_path = in_path + '\\' + str(files[i])
            folder_check = os.path.isdir(abs_path)
            if folder_check is True:
                folder_list.append(abs_path)

            file_path.append(os.path.abspath(os.path.join(abs_path, os.pardir)) + '\\' + files[i])

        for i in range(0, len(folder_list)):
            file_list(folder_list[i])

        return file_path

    except:
        print("[Error] Path is not found. Check your input")

path = 'path'


def file_count(csv_file):
    count = len(csv_file)
    print(count)
    return count

def file_name(csv_file):
    count = file_count(csv_file)
    for i in range(0, count):
        print(csv_file[i])

def column_name(data):
    print(data.columns)

def read_data(file):
    f = open(file, 'r')
    data = csv.reader(f)
    for line in data:
        print(line)
    return data

# for i in range(0, 1000):
#     with open(file_list(path)[i], 'r') as f:
#         data = pd.read_csv(file_list(path)[i])
#         file = file_list(path)[i].split('\\')[9]
#         print('=========================[' + str(i) + ']===========================')
#         print(file)
#         print(data)
        # reader = csv.reader(f)
        # print('['+str(i)+']' + '' + str(file_list(path)[i].split('\\')[9]))
        # for txt in reader:
        #     print(txt)
        # print('===================================')

csv_file = file_list(path)[0]
cnt = file_count(csv_file)
read_data(csv_file)
file_name(csv_file)

