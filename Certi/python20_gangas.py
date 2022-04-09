import sys
from heapq import heappop, heappush
from collections import defaultdict

"""
스카우터

: 선수평가 업데이트

    기존 평가 확인 위해, 선수평가 기록을 가지고 있어야함 (pid, score)를 list로 가지고 있어야함. 
    그럼 이걸 확인하기 위한 자료형이 뭐가 있을까? list, dict가 있다. 
    list는 선형 검색이 필요하고, dict에는 pid: score로 처리도 가능하다. --> 아마 선형 탐색이라 성능 차이는 없을 것이다.

    1) 처음 평가 -> sum + score, cnt +1  -> avg 계산 필요
    2) 기존 평가 -> sum + score - orgScore, cnt  -> avg 계산 필요. 

    평가를 할 때 업데이트가 필요 -> heapq push (lazy Update의 개념이 필요) 

: 기록 업데이트 / 삭제 과정 필요.
    스카우터의 입장에서는 기록이 삭제됨.
        -> sum-score, cnt-1,  
    선수 입장에서는 업데이트가 됨.
        -> heapq push

선수 1 ~ 10,000 
1) sum, avg, cnt

q * n 을 하게 되면 10,000,000,000이 되서 TLE 발생한다. 

"""


# 스카우터 : 1 ~ 10,000
# 선수 : 1 ~ 10,000

class Player(object):
    sum, avg, cnt = 0,0,0

    def update(self, dsum, dcnt):
        self.sum += dsum
        self.cnt += dcnt
        self.avg = round(self.sum / self.cnt) if self.cnt else 0


    def __repr__(self):
        return f'Player : {self.sum}, {self.avg}, {self.cnt}'


def push(pid):
    heappush(maxsum, (-P[pid].sum, -pid))
    heappush(minsum, (P[pid].sum, pid))
    heappush(maxavg, (-P[pid].avg, -pid))
    heappush(minavg, (P[pid].avg, pid))

# sys.stdin = open("input.txt")
input = sys.stdin.readline
n,m = map(int,input().split())

#자료형 만드는 중
maxsum, minsum, maxavg, minavg = [],[],[],[]
#스카우터
S = [defaultdict(int) for _ in range(n+1)]
P = [Player() for _ in range(m+1)]
for i in range(1, m+1) :
    push(i)


for _ in range(int(input().strip())):
    cmd = input().split()
    if cmd[0] == "EVAL" :
        sid, pid, score = map(int, cmd[1:])
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
        print(abs(pq[0][1]))

    else :
        pq = maxavg if cmd[1] == '1' else minavg
        while abs(pq[0][0]) != P[abs(pq[0][1])].avg : heappop(pq)# 기록된 값이 다른 경우에는 유효하지 않기 때문에 버려진다.
        print(abs(pq[0][1]))
























