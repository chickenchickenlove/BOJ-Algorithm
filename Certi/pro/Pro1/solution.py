'''
solution.py
1. 해싱으로 그 문자열이 나타나는 인덱스만 찾아둔다.
2. 그 인덱스를 기준으로 일치하는 값이 몇개 있는지 찾아본다.
'''

from collections import deque, defaultdict

que = deque()
RD = defaultdict(int)
D = defaultdict(int)
isReverse = 0

def init(mStr: str):
    global que, isReverse
    que = deque([i for i in mStr])

    for i in range(len(mStr)) :
        temp = ""
        for j in range(i,i+4) :
            if len(mStr) <= j : break

            temp += mStr[j]
            D[temp] +=1

    mStr = mStr[::-1]
    for i in range(len(mStr)) :
        temp = ""
        for j in range(i,i+4) :
            if len(mStr) <= j: break
            temp += mStr[j]
            RD[temp] +=1

def pushBack(mWord: str):
    global que, isReverse

    if isReverse :

        cnt = 2
        temp_str = deque([])
        while cnt >=0 :
            temp_str.appendleft(que[cnt])
            cnt -=1

        for c in mWord :
            que.appendleft(c)
            temp_str.appendleft(c)
        temp_str = (''.join(map(str,list(temp_str))))

    else :
        # 문자열 3개 모았다.
        cnt = 3
        temp_str = deque()
        while cnt > 0 :
            temp_str.append(que[len(que)-cnt])
            cnt -=1
        for c in mWord :
            que.append(c)
            temp_str.append(c)
        temp_str = ''.join(map(str,list(temp_str)))

    cal_push(temp_str, mWord)

def popBack(k: int):
    global que, isReverse

    temp_str = deque()
    if isReverse :
        for _ in range(k) :
            temp_str.appendleft(que.popleft())
        for i in range(3) :
            temp_str.appendleft(que[i])

    else :
        for _ in range(k) :
            temp_str.append(que.pop())
        for i in range(1,4) :
            temp_str.append(que[-i])

    cal_pop(''.join(map(str, list(temp_str))), k)




def cal_push(temp_str,mWord) :

    right_str = temp_str[::-1] if isReverse else temp_str
    reverse_str = temp_str if isReverse else temp_str[::-1]
    right_dict = RD if isReverse else D
    reverse_dict = D if isReverse else RD

    for i in range(len(right_str)):
        temp = ""
        for j in range(i, i + 4):
            if j >= len(right_str): break
            temp += temp_str[j]
            if i == 0:
                if j - i >= 3:
                    right_dict[temp] += 1
            elif i == 1:
                if j - i >= 2:
                    right_dict[temp] += 1
            elif i == 2:
                if j - i >= 1:
                    right_dict[temp] += 1
            else:
                right_dict[temp] += 1

    for i in range(len(mWord)):
        check_str = reverse_str[i:i + 4]
        for j in range(len(check_str)):
            # print(check_str[:len(check_str)-j])
            reverse_dict[check_str[:len(check_str)-j]] += 1


def cal_pop(temp_str,k) :

    right_str = temp_str[::-1] if isReverse else temp_str
    reverse_str = temp_str if isReverse else temp_str[::-1]
    right_dict = RD if isReverse else D
    reverse_dict = D if isReverse else RD


    for i in range(len(right_str)) :
        temp = ""
        for j in range(i, i+4) :
            if j >= len(right_str) : break
            temp += temp_str[j]
            if i == 0 :
                if j-i >= 3 :
                    right_dict[temp] -=1
            elif i == 1 :
                if j - i >= 2 :
                    right_dict[temp] -=1
            elif i == 2 :
                if j-i >= 1 :
                    right_dict[temp] -=1
            else :
                right_dict[temp] -=1


    for i in range(k) :
        check_str = reverse_str[i:i+4]
        for j in range(len(check_str)) :
            # print(check_str[:len(check_str)-j])
            reverse_dict[check_str[0:len(check_str)-j]] -=1









def reverseStr():
    global que, isReverse
    isReverse = (isReverse + 1 ) % 2


def getCount(mWord: str) -> int:
    global que, isReverse
    # print(que)
    if isReverse :
        print(RD[mWord])
        return RD[mWord]
    else :
        print(D[mWord])
        return D[mWord]
