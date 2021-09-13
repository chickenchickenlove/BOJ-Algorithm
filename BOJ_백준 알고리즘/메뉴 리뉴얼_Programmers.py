import itertools
from collections import defaultdict
from collections import Counter


#1. orders를 입력받아서 조합으로 default dict를 만든다.



def solution(orders, course):
    answer = []



    for c in course :
        temp = []
        for order in orders :
            combi = itertools.combinations(sorted(order),c)
            temp += combi

        my_dict = Counter(temp)

        if len(my_dict) > 0 :

            max_ = max(list(my_dict.values()))
            if max_ >= 2 :
                for key_, values_ in my_dict.items() :
                    if values_ == max_ :
                        answer.append(''.join(map(str,key_)))




    answer = sorted(answer)
    print(answer)

    return answer


solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5] )