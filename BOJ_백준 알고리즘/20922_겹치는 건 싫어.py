import sys

# 입력
n,k = map(int,sys.stdin.readline().split())
my_list = list(map(int,sys.stdin.readline().split()))



# 변수 초기화
l,r,ans,c_cnt, temp_cnt = 0,-1,0,0,0
num_list = [0 for _ in range(100000 + 1)]
mem_list = [set() for _ in range(200000 + 1)]
for i in my_list:
    mem_list[0].add(i)

while True :

    # 문자열 상태 판별
    if c_cnt <= k :
        ans = max(ans,temp_cnt)

    # 두 포인터 이동
    if c_cnt <= k :
        r +=1
        if r >= n :
            break

        # R이 가리키는 현재 숫자를 가져온다.
        now_num = my_list[r]

        # R이 가리키는 현재 숫자의 카운트를 올린다.
        num_list[now_num] += 1
        c_cnt = max(c_cnt, num_list[now_num])

        # 현재 수열의 길이를 증가시킨다.
        temp_cnt +=1


        # 현재 숫자의 카운트가 얼마인지 본다.
        now_num_cnt = num_list[now_num]
        pre_num_cnt = now_num_cnt-1

        # 집합에 초기화 한다
        # 1. 이전에 있었던 건 집합에서 제거한다
        # 2. 현재 위치를 집합에 추가한다.
        mem_list[now_num_cnt].add(now_num)
        mem_list[pre_num_cnt].remove(now_num)




    else :
        # l이 가리키는 현재 숫자가 무엇인지 가져온다.
        now_num = my_list[l]

        # 현재 숫자 카운트를 가져온다
        now_num_cnt = num_list[now_num]
        num_list[now_num] -= 1
        # 다음 숫자 카운트를 가져온다.
        next_num_cnt = now_num_cnt - 1

        # 업데이트 해준다.

        mem_list[now_num_cnt].remove(now_num)
        mem_list[next_num_cnt].add(now_num)

        # 현재 위치 카운트가 0이면, 얘가 최대값이다.
        if len(mem_list[now_num_cnt]) == 0 and now_num_cnt == c_cnt:
            c_cnt = next_num_cnt

        l += 1
        if l > r :
            break
        temp_cnt -=1




print(ans)





