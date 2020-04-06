import re

f = open('co_block2.txt','rb')
lines = f.readlines()
for line in lines:
    item = line.split()
    rowid = item[0]
    print(rowid)




