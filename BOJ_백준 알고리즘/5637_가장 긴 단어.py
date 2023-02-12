import sys


#단어의 종결을 보여주는 것 . , ! (



my_str = ''
max_str = 0
answer_str = ''
while 1 :
    temp = str(sys.stdin.readline().rstrip())
    for i in temp :
        if not i.isalpha() or i.isdigit() :
            if i != '-' :
                if len(my_str) > max_str :
                    max_str = len(my_str)
                    answer_str = my_str
                my_str = ''
            elif i == '-' :
                my_str +=i

        else :
            my_str += i
        if len(my_str) == 5 :
            if my_str == 'E-N-D' :
                for i in answer_str :
                    if 50<= ord(i) <= 90 :
                        print(chr(ord(i) + 32), end='')
                    elif ord(i) == 45:
                        print(i,end ='')
                    else :
                        print(i,end = '')
                exit()
    if len(my_str)>0 :
        if my_str[-1] != '-' :
            if len(my_str) > max_str :
                max_str = len(my_str)
                answer_str = my_str
            my_str = ''


