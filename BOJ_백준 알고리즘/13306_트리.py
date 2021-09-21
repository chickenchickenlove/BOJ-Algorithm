import sys
sys.setrecursionlimit(500000)

# 루트는 무조건 1이다. (부모노드)
# 검사하는 방법, 둘다 1로 가는 길이 있는지 확인한다.
# 제거하는 방법, 7,11 사이의 에지를 제거하면, 자식 노드에 스스로 노드를 저장한다. 그리고 다른 노드의 루트노드가 1인지 확인한다.
# 끝나면, 다시 에지를 원상복귀 해준다.


def find(a) :
    if d[a] == a :
        return a
    else :
        d[a] = find(d[a])
        dd[a] = d[a]
        return d[a]

def union(a,b) :
    a,b = find(a), find(b)
    if a == b :
        return
    else :
        d[a] = b
        return



n,q = map(int,sys.stdin.readline().split())

d = [i for i in range(n+1)]
dd = [i for i in range(n+1)]
for k in range(2, n+1) :
    dd[k] = int(sys.stdin.readline().rstrip())


temp = []
for _ in range(n-1 + q) :
    temp.append(list(map(int,sys.stdin.readline().split())))



answer = []
while temp :
    command = temp.pop()

    # union 한다.
    if command[0] == 0 :
       a,b = command
       d[b] = dd[b]


    else :
        a,b,c = command

        if find(b) == find(c)  :

            answer.append('YES\n')
        else :

            answer.append('NO\n')

while answer :
    sys.stdout.write(answer.pop())
