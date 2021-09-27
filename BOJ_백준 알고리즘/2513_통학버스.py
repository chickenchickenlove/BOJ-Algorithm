import sys
n,k,s = map(int,sys.stdin.readline().split())
my_list = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
my_list = sorted(my_list, key = lambda x : x[0])

answer = 0
bus = 0
temp = 0
last_idx = -1
for idx in range(len(my_list)) :
    if my_list[idx][0] >= s:
        answer += temp * 2
        temp = 0
        last_idx = idx
        break

    if bus == 0:
        temp = abs(s - my_list[idx][0])
    elif bus == k:
        answer += temp * 2
        temp = abs(s - my_list[idx][0])
        bus = 0


    # 버스를 더 태울 수 있는 상태
    # 버스에 사람을 태운다.
    # 이 때가 최대임
    if my_list[idx][1] + bus <= k:
        bus += my_list[idx][1]
        my_list[idx][1] = 0
        temp = max(temp, abs(s - my_list[idx][0]))

    elif my_list[idx][1] + bus > k:
        while my_list[idx][1] != 0:
            p_value = k - bus
            if my_list[idx][1] - p_value < 0:
                bus = my_list[idx][1]
                my_list[idx][1] = 0

            elif my_list[idx][1] - p_value == 0 :
                bus = 0
                my_list[idx][1] = 0
                answer += temp * 2
                temp = 0
                break

            else:
                answer += temp * 2
                my_list[idx][1] -= p_value
                bus = 0


            temp = abs(s - my_list[idx][0])

answer += temp * 2


if last_idx == -1 :
    print(answer)
    exit()

bus = 0
temp = 0



for idx in range(len(my_list)-1, last_idx-1,-1) :
    if my_list[idx][0] <= s :
        answer += temp * 2
        temp = 0
        last_idx = idx
        break

    if bus == 0 :
        temp = abs(s-my_list[idx][0])
    elif bus == k :
        answer += temp * 2
        temp = abs(s - my_list[idx][0])
        bus = 0

    if my_list[idx][1] + bus <= k :
        bus += my_list[idx][1]
        my_list[idx][1] = 0
        temp = max(temp, abs(s-my_list[idx][0]))
    elif my_list[idx][1] + bus > k :

        while my_list[idx][1] != 0 :

            p_value = k - bus
            if my_list[idx][1] - p_value < 0 :
                bus = my_list[idx][1]
                my_list[idx][1] = 0
            elif my_list[idx][1] - p_value == 0 :
                bus = 0
                my_list[idx][1] = 0
                answer += temp * 2
                temp = 0
                break

            else :
                answer += temp * 2
                my_list[idx][1] -= p_value
                bus = 0

            temp = abs(s - my_list[idx][0])

answer += temp*2
print(answer)










