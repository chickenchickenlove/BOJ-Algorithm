import sys
from heapq import heappop, heappush
from collections import defaultdict

class Player(object):
    sum, avg, cnt = 0,0,0
    name = ""

    def update(self, dsum, dcnt):
        self.sum += dsum
        self.cnt += dcnt
        self.avg = round(self.sum / self.cnt, 1) if self.cnt else 0

    def __repr__(self):
        return f'Player : {self.sum}, {self.avg}, {self.cnt}'


#문자값을 Max값으로 정렬될 수 있도록 한다.
class MaxData(object):
    def __init__(self, priority, name):
        self.priority = priority
        self.name = name
    # MaxData Type의 비교를 설정하려면 이걸 오버라이딩 해줘야함.
    def __lt__(self,  rhs): # < Self 기준으로 Operator가 동작한다.
        if self.priority != rhs.priority :
            # 가장 작은 값이 Top으로 오게 해야하기 때문에, 큰게 작다라고 정리해준다.
            return self.priority > rhs.priority
        return self.name > rhs.name

class MinData(object):
    def __init__(self, priority, name):
        self.priority = priority
        self.name = name
    # MaxData Type의 비교를 설정하려면 이걸 오버라이딩 해줘야함.
    def __lt__(self,  rhs): # < Self 기준으로 Operator가 동작한다.
        if self.priority != rhs.priority :
            # 가장 작은 값이 Top으로 오게 해야하기 때문에, 큰게 작다라고 정리해준다.
            return self.priority < rhs.priority
        return self.name < rhs.name



def push(pid):
    heappush(maxsum, (-P[pid].sum, -pid))
    heappush(minsum, (P[pid].sum, pid))
    heappush(maxavg, (-P[pid].avg, -pid))
    heappush(minavg, (P[pid].avg, pid))


def push(pid):
    heappush(maxsum, (-P[pid].sum, -pid))
    heappush(minsum, (P[pid].sum, pid))
    heappush(maxavg, (-P[pid].avg, -pid))
    heappush(minavg, (P[pid].avg, pid))

# sys.stdin = open("input.txt")
input = sys.stdin.readline
n,m = map(int,input().split())



# 딕셔너리로 생성
S = defaultdict(dict) # S[sid] = dict{key:pid / value: score}
P = [Player() for _ in range(m+1)]
maxsum, minsum, maxavg, minavg = [],[],[],[]


#이름을 입력 받는다.
name = list(input().split())
name.sort()
nameDict = {}
for i in range(1, m+1) :
    nameDict[name[i-1]] = i
    P[i].name = name[i-1]
    push(i)

for _ in range(int(input().strip())):
    cmd = input().split()
    if cmd[0] == "EVAL" :
        sid, pname, score = int(cmd[1]), cmd[2], int(cmd[3])
        pid = nameDict[pname]

        #있는 경우면 업데이트 해준다.
        if pid in S[sid] : P[pid].update(score-S[sid][pid],0)
        else : P[pid].update(score,1)
        S[sid][pid] = score
        push(pid)

    elif cmd[0] == "CLEAR" :
        sid = int(cmd[1])
        for pid, score in S[sid].items() :
            P[pid].update(-score, -1)
            push(pid)
        S[sid].clear()

    elif cmd[0] == "SUM" :
        pq = maxsum if cmd[1] == '1' else minsum
        while abs(pq[0][0]) != P[abs(pq[0][1])].sum : heappop(pq)# 기록된 값이 다른 경우에는 유효하지 않기 때문에 버려진다.
        print(P[abs(pq[0][1])].name)

    else :
        pq = maxavg if cmd[1] == '1' else minavg
        while abs(pq[0][0]) != P[abs(pq[0][1])].avg : heappop(pq)# 기록된 값이 다른 경우에는 유효하지 않기 때문에 버려진다.
        print(P[abs(pq[0][1])].name)