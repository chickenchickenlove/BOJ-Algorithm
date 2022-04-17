global remainId

def find(x, query):
    s, e = 0, len(remainId)
    while e-s>5:
        mid = max(s+5, (s+e)//2)
        if query(mid-s, remainId[s:mid], 0) == x: e = mid
        else: s = mid

    for i in range(s,e):
        if query(len(remainId) - 1, remainId[:i] + remainId[i+1:], 0) != x:
            return remainId[i]

def getRank(retRank: [int], query) -> None:
    global remainId
    remainId = list(range(1000))
    minId = []
    for i in range(4):                  # rank 0~3인 id 구하기
        minId.append(find(i, query))    # find(i) : rank가 i인 id 반환
        retRank[minId[i]] = i
        remainId.remove(minId[i])
    for x in remainId:                  # rank 4~999인 id 구하기
        retRank[x] = query(5, minId+[x], 1)
    # print(retRank)