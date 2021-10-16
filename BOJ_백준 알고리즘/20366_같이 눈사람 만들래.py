import sys


n = int(sys.stdin.readline().rstrip())
my_list = sorted(list(map(int,sys.stdin.readline().split())))
answer = 9876543210

for i in range(n-1) :
    for j in range(i+1,n) :
        now_sum = my_list[i] + my_list[j]
        l,r = 0, n-1
        while l == i or l == j :
            l +=1
        while r == i or r == j :
            r -=1
        while l < r :
            new_sum = my_list[l] + my_list[r]
            if new_sum > now_sum :
                r -= 1
                while r == j or r == i :
                    r -=1
            elif new_sum == now_sum :
                print(0)
                exit()
            else :
                l +=1
                while l == j or l == i :
                    l +=1


            if abs(now_sum-new_sum) < answer :
                answer = abs(now_sum - new_sum)

print(answer)