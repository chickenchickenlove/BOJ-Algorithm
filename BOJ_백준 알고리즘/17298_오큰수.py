

n = int(input())
num_list = list(map(int,input().split()))
trash_list = []
answer_li = [-1 for i in range(0,n)]

for index_no in range(n-1) :
    if num_list[index_no] < num_list[index_no + 1] :
        answer_li[index_no] = num_list[index_no + 1]
        if len(trash_list) != 0 :
            while num_list[trash_list[-1]] < num_list[index_no + 1] :
                answer_li[trash_list.pop()] = num_list[index_no + 1]
                if len(trash_list) == 0 :
                    break
    else :
        trash_list.append(index_no)



for p in answer_li :
    print(p, end=' ')

