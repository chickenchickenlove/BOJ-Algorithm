import sys
from collections import defaultdict

def resolver(r,c):
    return ",".join(map(str,(r,c)))



n,q = map(int,sys.stdin.readline().split())
player = [0 for _ in range(5)]
earth = defaultdict(int)
player_cnt = 1
for _ in range(q):
    r,c = map(int,sys.stdin.readline().split())
    # r,c = r-1, c-1

    key = r * n + c

    #땅이 점령되지 않은 경우
    if earth[key] == 0 :

        earth[key] = player_cnt
        player[player_cnt] +=1

    #땅이 본인 땅인 경우
    elif earth[key] == player_cnt :
        #땅을 반납한다.
        earth[key] = 0
        player[player_cnt] -=1
    else :
        own_player = earth[key]
        if player[own_player] > player[player_cnt] :
            earth[key] = player_cnt
            player[player_cnt] += 1
            player[own_player] -= 1

    player_cnt +=1
    if player_cnt >= 5 : player_cnt = 1

for i in player[1:] :
    print(i)