import sys
for _ in range(int(sys.stdin.readline().rstrip())):
    n,m = map(int,sys.stdin.readline().split())
    v = [0 for _ in range(n+1)]
    book_list = [list(map(int,sys.stdin.readline().split())) for _ in range(m)]
    book_list = sorted(book_list, key = lambda x : (x[1],x[0]))
    answer = 0
    for s,e in book_list :
        for i in range(1,n+1) :
            if s <= i <= e and v[i] == 0 :
                v[i] =1
                answer +=1
                break
    print(answer)



