import sys
from collections import deque




def my_insert(cursor, mystr):
    global n,m, my_cnt
    my_cnt +=1
    r,c = cursor
    cursor = (r,c+1)
    note[r].insert(c,mystr)
    while len(note[r]) > m :
        note[r+1].appendleft(note[r].pop())
        r += 1
    return cursor

def my_erase(cursor):
    global n,m, my_cnt
    my_cnt -=1
    r,c = cursor
    del note[r][c]
    while len(note[r+1]) != 0 :
        note[r].append(note[r+1].popleft())
        r +=1
    c -=1
    return cursor


def my_move(r,c):
    global m
    cursor = r,c

    if r*m  + c >= my_cnt :
        r = my_cnt // m
        c = my_cnt % m
        print("*")
        cursor = r,c
    else :
        print(note[r][c])
    return cursor



def print_note():
    for k in note:
        print(k)
    print()


n,m,q = map(int,sys.stdin.readline().split())
note = [deque() for _ in range(m)]
cursor = (0,0)

my_cnt = 0
row = 0
for c in sys.stdin.readline().rstrip() :
    if len(note[row]) >= m :
        row += 1
    note[row].append(c)
    my_cnt+=1

for _ in range(q) :
    cmd = list(map(str,sys.stdin.readline().split()))

    if cmd[0] == "insert" :
        cursor = my_insert(cursor, cmd[1])
    if cmd[0] == "move" :
        cursor = my_move(*map(int,(cmd[1], cmd[2])))
    if cmd[0] == "erase":
        cursor = my_erase(cursor)
