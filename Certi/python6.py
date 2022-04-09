import sys

con_list = []
for _ in range(int(sys.stdin.readline().rstrip())) :
    a,s,e = map(int,sys.stdin.readline().split())
    con_list.append((a,s,e))

con_list.sort(key = lambda x : [x[2], x[1]])
answer_list = []
answer_list.append([*con_list[0]])


for a,s,e in con_list[1:] :
    if answer_list[-1][2] <= s :
        answer_list.append([a,s,e])

    elif answer_list[-1][1] <= s and e <= answer_list[-1][2] :
        answer_list.pop()
        answer_list.append([a, s, e])

    elif answer_list[-1][2] <= s  and answer_list[-1][1] >= e:
        answer_list.append([a, s, e])


print(len(answer_list))
my_list = [a for a,b,c in answer_list]
print(*my_list)