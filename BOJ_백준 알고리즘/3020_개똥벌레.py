import sys



n,h = map(int,sys.stdin.readline().split())
odd = []
even = []

for q in range(n) :
    if q %2 == 0 :
        even.append(int(sys.stdin.readline().rstrip()))
    else :
        odd.append(int(sys.stdin.readline().rstrip()))


ed = [0 for _ in range(h+1)]
od = [0 for _ in range(h+1)]

for a in even :
    ed[a] +=1
for a in odd :
    od[a] +=1

for i in range(h,0,-1) :
    ed[i-1] += ed[i]
    od[i-1] += od[i]

pd = []
for i in range(1,h+1) :
    temp = od[h-i + 1] + ed[i]

    pd.append(temp)
pd = sorted(pd)

answer = pd[0]
cnt = 0
for k in pd :
    if k == answer :
        cnt +=1
    else :
        break
print(answer, cnt)
