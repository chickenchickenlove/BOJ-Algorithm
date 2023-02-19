import sys

test_case = int(sys.stdin.readline().rstrip())
person_li = []
answer_li = []

for person in range(test_case) :
    person_li.append(list(map(int,input().split())))

cnt = 0

for i in range(test_case) :
    for p in range(test_case) :
        if person_li[i][0] < person_li[p][0] and person_li[i][1] < person_li[p][1] :
            cnt += 1
    answer_li.append(str(cnt+1))
    cnt = 0

print(' '.join(answer_li))