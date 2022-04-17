global remainId
def binary_search(query, x):
    l, r = 0, len(remainId)-1
    while l <= r:
        mid = (l + r) // 2
        temp_list = remainId[l:mid+1]
        if len(temp_list) < 5 : break
        if query(len(temp_list), temp_list, 0) == x : r = mid
        else: l = mid

    for i in range(l,r+1) :

        # 이 부분 생각 바꿔야 함.
        # 이렇게 슬라이싱으로 접근을 했는데, 처음에는 어디서부터 시작했는지 모르니..
        # 이걸 또 분기문을 나눠서 처리를 했었다.
        t = remainId[:i] + remainId[i+1:]
        k = len(t)
        if query(k,t,0 ) != x :
            return remainId[i]

def getRank(retRank: [int], query) -> None:
    global remainId

    min_value = []
    remainId = list(range(1000))

    for x in range(4) :
        min_value.append(binary_search(query,x))
        remainId.remove(min_value[-1])

        # 이 부분에서 랭크를 잘못 처리했었다.
        retRank[min_value[-1]] = x

    # 이 부분에서 0 ~ 1000까지 돌리면서 코드를 번거롭게 만들었따.
    for x in remainId:
        retRank[x] = query(5, min_value + [x], 1)

    # print(retRank)
