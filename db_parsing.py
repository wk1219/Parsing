f = open('co_block2.txt','rb')
lines = f.readlines()
db_row = []
for line in lines:
    item = line.split()
    rowid = item[0]
    time = item[1]
    user = item[2]
    rollback = str(item[3])
    wid = item[4]
    x = item[5]
    y = item[6]
    z = item[7]
    db_row = [rowid, time, user, rollback, wid, x, y, z]
    if rollback == "b'1,'":
        print(db_row)




