def sol(i) :
    global answer
    if '666' in str(i) :
        answer.append(i)


n = int(input())
answer = []
i = 666

while len(answer) < n  :
    sol(i)
    i += 1

print(answer[n-1])

