import sys
n = int(sys.stdin.readline().rstrip())
rope_list = list()
for p in range(n) :
    rope_list.append(int(sys.stdin.readline().rstrip()))

rope_list = sorted(rope_list, reverse = True)
cnt = 0

for i in range(n) :
    if cnt == 0 :
        last_max = rope_list[i] * (i+1)
        cnt += 1
    else :
        if rope_list[i] * (i+1) > last_max :
            last_max = rope_list[i] * (i+1)

print(last_max)
