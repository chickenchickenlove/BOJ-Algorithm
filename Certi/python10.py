import sys
from collections import defaultdict

def cmd1(user):
    return user_dict[user]

def cmd2(user):
    return login_dict[user]

def cmd3(user):
    global user_cnt
    if not user_dict[user] :
        user_dict[user] = 1
        user_cnt += 1
    return user_cnt

def cmd4(user):
    global user_cnt, login_cnt
    if user_dict[user] :
        user_dict[user] = 0
        user_cnt -=1
        if login_dict[user] :
            login_dict[user] = 0
            login_cnt -= 1
    return user_cnt

def cmd5(user):
    global user_cnt, login_cnt
    if user_dict[user] and (not login_dict[user]) :
        login_dict[user] = 1
        login_cnt +=1
    return login_cnt

def cmd6(user):
    global user_cnt, login_cnt
    if user_dict[user] and login_dict[user]:
        login_dict[user] = 0
        login_cnt -=1
    return login_cnt

user_dict = defaultdict(int)
login_dict = defaultdict(int)
user_cnt, login_cnt = 0,0

for _ in range(int(sys.stdin.readline().rstrip())) :
    a,user = map(str,sys.stdin.readline().split())

    if a == "1":
        print(cmd1(user))
    elif a == "2":
        print(cmd2(user))
    elif a == "3":
        print(cmd3(user))
    elif a == "4":
        print(cmd4(user))
    elif a == "5":
        print(cmd5(user))
    elif a == "6":
        print(cmd6(user))