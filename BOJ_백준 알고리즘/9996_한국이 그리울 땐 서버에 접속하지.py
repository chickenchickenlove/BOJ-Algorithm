import sys
t = int(sys.stdin.readline().rstrip())
temp = str(sys.stdin.readline().rstrip())
flag = 'F'
pre_s =''
post_s =''
for i in temp :
    if i == '*' :
        flag = 'T'
    elif flag == 'F' :
        pre_s += i
    elif flag == 'T' :
        post_s += i

post_s = post_s[::-1]

for i in range(t) :
    k = - 1
    j = - 1
    temp = str(sys.stdin.readline().rstrip())
    k = temp.find(pre_s)
    h = temp[k+len(pre_s):][::-1]
    j = h.find(post_s)
    if k == 0 and j == 0 :
        print('DA')
    else :
        print('NE')