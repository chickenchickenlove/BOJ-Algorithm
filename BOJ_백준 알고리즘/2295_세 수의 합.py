# 딕셔너리로 200ms에 푸는 방법이 있음.



import sys
n = int(sys.stdin.readline().rstrip())
my_list = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
list1, list2 = [],[]

for i in my_list :
    for j in my_list :
        list1.append(i + j )
        list2.append((j-i,j))
list1,list2 = sorted(list1), sorted(list2)


answer = 0
for target in list1 :

    l = 0
    r = len(list2) -1
    while l <= r :
        m = (l+r)//2
        if list2[m][0] == target :
           answer = max(answer, list2[m][1])
           break
        elif list2[m][0] < target :
            l = m +1
        else :
            r = m - 1

print(answer)




