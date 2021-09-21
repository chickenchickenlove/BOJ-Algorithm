import sys



# 분리집합으로 푼다.
# 진실을 아는 사람과 절대 그룹을 만들면 안된다.
# 같은 파티에 오는 사람들은 같은 그룹이 된다.
# 일단 진실을 아는 사람들끼리는 union을 한다.
# 그리고 각 파티마다 union을 한다.
# 파티가 끝난 후, 앞에서부터 각 파티의 1번이 진실을 아는 사람과 같은 그룹인지 확인한다.
# 아니면, 그 파티는 cnt + 1 한다

def init(n) :
    d = [i for i in range(n+1)]
    return d


def find(a) :
    if d[a] == a :
        return a
    else :
        d[a] = find(d[a])
        return d[a]


def union(a,b) :
    a = find(a)
    b = find(b)

    if a == b :
        pass
    else :
        if rank[a] >= rank[b] :
            rank[a] += rank[b]
            rank[b] = 0
            d[b] = a
        else :
            rank[b] += rank[a]
            rank[a] = 0
            d[a] = b
        return

n,m = map(int,sys.stdin.readline().split())


d = [i for i in range(51)]
rank = [1 for _ in range(51)]

know_list1 = list(map(int,sys.stdin.readline().split()))
if know_list1[0] > 0 :
    for i in range(1, len(know_list1) - 1 ):
        union(know_list1[i], know_list1[i+1])


stack = []
for _ in range(m) :
    know_list = list(map(int,sys.stdin.readline().split()))
    if know_list[0] > 0 :
        for i in range(1, len(know_list) - 1):
            union(know_list[i], know_list[i + 1])
        stack.append(know_list[1])

answer = 0
union_pull = set()
for kk in know_list1[1:] :
    union_pull.add(find(kk))
while stack :
    a = stack.pop()
    k = find(a)
    if k not in union_pull :
        answer +=1

print(answer)


