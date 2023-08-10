import sys
from collections import defaultdict


tree_dict = defaultdict(int)
cnt = 0
while 1 :
    try :
        wood_name = str(sys.stdin.readline().rstrip())
        if wood_name == '':
            break
        tree_dict[wood_name] +=1
        cnt +=1
    except :
        break

answer_list = []
for key, values in tree_dict.items() :
    name = key
    percent = (values) / cnt * 100
    answer_list.append((name, percent))

answer_list = sorted(answer_list)
for a,b in answer_list :
    print(f'{a} {b:.4f}')



