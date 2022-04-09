import sys
def sol(last_num, temp_sum) :
    dn = 1
    while 1 :
        start = dice_list[dn].index(last_num)
        end = find_end(start)

        start_value, end_value = dice_list[dn][start], dice_list[dn][end]

        # 이런 두 가지 방법으로 처리를 할 수 있음.
        # temp_sum += max(filter(lambda x : x not in (start_value, end_value), dice_list[dn]))
        temp_sum += max(dice_list[dn], key = lambda x : 0 if x in (start_value, end_value) else x)
        last_num = dice_list[dn][end]
        dn +=1

        if dn == len(dice_list) :
            break
    return temp_sum


n = int(sys.stdin.readline().rstrip())
dice_list = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

def find_end(start) :
    if start == 0 : return 5
    if start == 1 : return 3
    if start == 2 : return 4
    if start == 3 : return 1
    if start == 4 : return 2
    if start == 5 : return 0

ans = 0

for start in range(6) :
    end = find_end(start)
    temp_sum, max_value = 0,0
    for idx, value in enumerate(dice_list[0]):
        if idx != start and idx != end :
            max_value = max(max_value, value)
    temp_sum = max_value
    ans = max(sol(dice_list[0][end], temp_sum), ans)

print(ans)