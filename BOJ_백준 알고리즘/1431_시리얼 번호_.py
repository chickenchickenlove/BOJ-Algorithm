import sys
n = int(sys.stdin.readline().rstrip())
num_list = []

for p in range(n) :
    num = 0
    name = str(sys.stdin.readline().rstrip())
    for p in name :
        if p.isdigit():
            num += int(p)
    length = len(name)
    num_list.append([name, length, num])

num_list = sorted(num_list, key = lambda x : (x[1], x[2], x[0]))

for p in range(len(num_list)) :
    print(num_list[p][0])