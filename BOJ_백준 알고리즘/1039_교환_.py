import sys
from collections import deque


#i,j 자릿수에 있는 숫자를 바꿔주는 함수
def swap(n,i,j,limit) :

    temp1 = (n // 10 ** i) % 10
    temp2 = (n // 10 ** j) % 10
    answer = n + (temp1 * 10 **j) + (temp2 * 10 **i) - (temp1 * 10 ** i) - (temp2 * 10 ** j)

    if len(str(answer)) != limit :
        return -1
    else :
        return answer



def bfs(n,k,limit) :

    #변수 선언
    que = deque()
    que.append((n,0))
    answer = -1

    #방문 배열 관리
    #동일한 곳에 2번 단위로 방문 가능하기 때문에 홀/짝 배열로 관리

    v_odd = [0 for _ in range(10000000+1)]
    v_even = [0 for _ in range(10000000+1)]


    #bfs로 짛냉
    while que :
        now_num, now_cnt = que.popleft()

        for i in range(limit-1) :
            for j in range(i+1,limit) :
                next_num = swap(now_num,i,j,limit)


                #다음 카운트가 홀수일 때,
                if (now_cnt + 1) % 2 == 1 :

                    #다음 카운트가 마지막 카운트가 아니고, 이전 방문 배열의 카운트보다 다음 카운트가 클 때
                    if next_num != -1 and now_cnt + 1 < k and v_even[next_num] < now_cnt + 1 :
                        que.append((next_num, now_cnt + 1))
                        v_even[next_num] = now_cnt + 1

                    #다음 카운트가 마지막이라면 답에 기록함
                    elif next_num != -1 and now_cnt + 1 == k:
                        answer = max(answer, next_num)

                #다음 카운트가 짝수일 때
                else :
                    # 다음 카운트가 마지막 카운트가 아니고, 이전 방문 배열의 카운트보다 다음 카운트가 클 때
                    if next_num != -1 and now_cnt + 1 < k and v_odd[next_num] < now_cnt + 1 :
                        que.append((next_num, now_cnt + 1))
                        v_odd[next_num] = now_cnt + 1

                    # 다음 카운트가 마지막이라면 답에 기록함
                    elif next_num != -1 and now_cnt + 1 == k:
                        answer = max(answer, next_num)


    print(answer)



#변수 입력
n,k = map(int,sys.stdin.readline().split())

#히든 케이스 처리
if n < 10 and k > 0 :
    print(-1)
elif n < 10 and k == 0  :
    print(n)
else :
#전체 관련 처리
    limit = len(str(n))
    bfs(n,k,limit)