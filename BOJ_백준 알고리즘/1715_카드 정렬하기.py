import sys
import heapq

my_list = []
for i in range(int(sys.stdin.readline().rstrip())) :
    my_list.append(int(sys.stdin.readline().rstrip()))
heapq.heapify(my_list)
answer = 0
while len(my_list) != 1 :
    a = heapq.heappop(my_list)
    b = heapq.heappop(my_list)
    heapq.heappush(my_list,a+b)
    answer += (a+b)
    if len(my_list) == 1 :
        break

print(answer)