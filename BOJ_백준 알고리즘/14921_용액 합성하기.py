import sys
n = int(sys.stdin.readline().rstrip())
my_list = sorted(list(map(int,sys.stdin.readline().split())))
l,r,answer = 0,len(my_list)-1,9876543210
while l < r :
    temp = my_list[l] + my_list[r]
    if temp >= 0 : r -=1
    else : l +=1
    if abs(answer) > abs(temp) : answer = temp
print(answer)