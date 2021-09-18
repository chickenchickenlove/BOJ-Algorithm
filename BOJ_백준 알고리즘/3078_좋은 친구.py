import sys
from collections import defaultdict
#좋은 친구
# A-B <= K , 문자열 길이 같음.

# 딕셔너리를 여러개 만든다.
# 문자열 길이 딕셔너리 = [] 순번을 넣는다.
# 각 문자열 딕셔너리에 대해 For문을 돌려서 갯수를 확인한다.

n,k = map(int,sys.stdin.readline().split())
char_dict = defaultdict(list)
for i in range(1,n + 1) :
    char = str(sys.stdin.readline().rstrip())
    idx = len(char)
    char_dict[idx].append(i)


answer = 0
for idx_list in char_dict.values() :

    cnt = 1
    for now_idx in range(len(idx_list)) :
        while now_idx + cnt < len(idx_list) :
            if idx_list[now_idx + cnt] - idx_list[now_idx] > k :
                break
            cnt +=1
        cnt -=1
        answer += cnt

print(answer)