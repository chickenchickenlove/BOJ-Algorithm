import sys
def cal(a,b):
    return a**2 - b**2

g = int(sys.stdin.readline().rstrip())
a,b = 1,1
not_answer = True

while a+b <= g:
    if cal(a,b) == g :
        print(a)
        a +=1
        not_answer = False
    elif cal(a,b) > g :
        b +=1
    elif cal(a,b) < g :
        a +=1

if not_answer :
    print(-1)





