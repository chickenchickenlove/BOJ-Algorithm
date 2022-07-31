import sys
e,s,m = map(int,sys.stdin.readline().split())
my_year = 1
E,S,M = 1,1,1

while 1 :
    if E == e and S == s and M ==m :
        print(my_year)
        break
    E +=1
    S +=1
    M +=1
    my_year +=1
    if E ==16 :
        E = 1
    if S == 29 :
        S = 1
    if M == 20 :
        M = 1