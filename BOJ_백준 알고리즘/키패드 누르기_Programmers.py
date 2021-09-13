# 왼손 : 1,4,7 (* 시작)
# 오른손 : 3,6,9 (# 시작)
# 2,5,8,0 현재 손가락에서 가까운 녀석을 사용함.
# 거리가 같다면 오른손 잡이는 오른손을 쓴다.

# 각 숫자에 대한 좌표를 설정한다.
# 좌표를 설정 후, 숫자가 들어오면 가가운 녀석을 위주로 보낸다.  (l,r)
# 조건식에서 왼속잡이 오른손잡이 고려한다.


def make_map() :
    my_map = [ [0 for _ in range(3)] for _ in range(4)]
    stack = ['#',0,'*',9,8,7,6,5,4,3,2,1,]


    for i in range(0,4) :
        for j in range(0,3) :
            my_map[i][j] = stack.pop()

    return my_map


def solution(numbers, hand):
    answer = ''
    key_pad = make_map()

    l = [3,0]
    r = [3,2]

    for num in numbers :
        if num in [1,4,7,'*']:
            for i in range(4) :
                for j in range(3) :
                    if key_pad[i][j] == num :
                        l = [i,j]
                        answer += 'L'
        elif num in [3,6,9,'#'] :
            for i in range(4) :
                for j in range(3) :
                    if key_pad[i][j] == num :
                        r = [i,j]
                        answer += 'R'
        else :
            for i in range(4) :
                for j in range(3) :
                    if key_pad[i][j] == num :
                        fr = [i,j]

            if abs((fr[0]-r[0])) + abs((fr[1] - r[1])) > abs((fr[0] - l[0])) + abs((fr[1] - l[1])) :
                a,b = fr
                l = [a,b]
                answer += 'L'
            elif abs(fr[0] - r[0]) + abs(fr[1] - r[1]) == abs(fr[0] - l[0]) + abs(fr[1] - l[1]):
                a,b = fr
                if hand == 'right' :
                    r = [a, b]
                    answer += 'R'
                else :
                    l = [a, b]
                    answer += 'L'
            elif abs((fr[0] - r[0])) + abs((fr[1] - r[1])) < abs((fr[0] - l[0])) + abs((fr[1] - l[1])):
                a, b = fr
                r = [a, b]
                answer += 'R'







    return answer




numbers =[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"
print(solution(numbers, hand))