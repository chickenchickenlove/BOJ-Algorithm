import sys
# 뒤에서부터 stack에 넣는다.
# 1. (가 나올 때까지 POP해서 STACK에 넣는다. 여기서 숫자는 숫자의 길이를 넣는다.
# 2. (가 나오면, )가 나올 때까지 STACK POP을 한다. 이 때 숫자는 따로 숫자에 저장해둔다.
# 3. 마지막 문자를 한번 더 기존 문자열에서 POP해서 곱한다. 그리고 STACK에 넣는다.
# 4. 1~3번 반복한다.
# 5. 마지막으로 stack이 0이 될 때까지 pop하며, pop의 원소들을 각각 더한다.

my_str = [c for c in str(sys.stdin.readline().rstrip())]

stack = []
while my_str :
    char = my_str.pop()
    if char != '(' :
        if char.isnumeric() :
            stack.append(1)
        else :
            stack.append(char)

    else :
        temp = 0
        while stack[-1] != ')' :
            temp += stack.pop()
        stack.pop()

        temp = int(my_str[-1]) * temp
        stack.append(temp)
        my_str.pop()
answer = 0
while stack :
    answer += stack.pop()

print(answer)