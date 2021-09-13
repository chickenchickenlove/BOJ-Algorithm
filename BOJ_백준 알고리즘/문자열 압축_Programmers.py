def make_sol(temp, pre_str) :
    last_str = ''
    answer = []
    cnt = 0
    for char in temp :
        if last_str == '' :
            last_str = char
            answer.append(char)
            cnt +=1
        else :
            if last_str == char :
                cnt +=1
            else :
                if cnt > 1 :
                    temp_str = answer.pop()
                    answer.append(cnt)
                    answer.append(temp_str)
                last_str = char
                answer.append(char)
                cnt = 1

    if cnt > 1:
        temp_str = answer.pop()
        answer.append(cnt)
        answer.append(temp_str)



    answer = pre_str + ''.join(map(str,answer))

    return len(answer)







def solution(s):
    answer = len(s)

    for len_ in range(1,len(s)) :



        temp = []
        start = 0
        end = start + len_

        pre_str = s[:start]
        while 1 :
            if end > len(s) :
                if s[start:] != '':
                    temp.append( s[start:])
                break
            else :
                temp.append(s[start:end])
            start += len_
            end = start + len_

        if len(temp) > 0 :
            answer = min(answer ,make_sol(temp,pre_str))


    return answer



s = "aabbaccc"
print(solution(s))

s = 'a'
print(solution(s))