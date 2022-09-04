import sys
from collections import deque


def sol(student_table, student_list,A) :

    v = [0 for _ in range(A+1)]
    answer = []

    que = deque()
    for no in range(len(student_table)) :

        if student_table[no] == 0 and no!= 0 :
            que.append(no)

    while que :
        now = que.popleft()
        answer.append(now)
        for no in student_list[now] :
            student_table[no] -=1
            if student_table[no] == 0 :
                que.append(no)

    return answer


my_list = []
A,B = map(int,sys.stdin.readline().split())
for _ in range(B) :
    my_list.append(list(map(int,sys.stdin.readline().split())))

student_table = [0 for _ in range(A+1)]
student_list = [[] for _ in range(A+1)]

for a,b in my_list :
    student_list[a].append(b)
    student_table[b] +=1

print(' '.join(map(str,sol(student_table,student_list,A))))