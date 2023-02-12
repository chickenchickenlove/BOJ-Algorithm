import sys

class Node(object) :
    def __init__(self,data):
        self.data = data
        self.child = {}
        self.flag = False



class Trie(object) :
    def __init__(self):
        self.head = Node(None)

    def insert(self,char):
        cur = self.head

        for c in char :
            if c not in cur.child :
                cur.child[c] = Node(c)
            cur = cur.child[c]
        cur.flag = True

    def count(self,char):
        cur = self.head
        return_value = 0

        for c in char :
            if cur == self.head :
                return_value +=1

            elif len(cur.child) > 1 or cur.flag == True :
                return_value +=1

            cur = cur.child[c]

        return return_value


while 1 :
    try :
        n = int(sys.stdin.readline().rstrip())
    except :
        exit()
    a = Trie()
    string_list = []
    answer = []
    for i in range(n) :
        my_str = str(sys.stdin.readline().rstrip())
        a.insert(my_str)
        answer.append(my_str)


    my_sum = 0

    for my_str in answer :
        my_sum += a.count(my_str)

    answer = my_sum / n
    answer = str(round(answer,2))
    a,b = answer.split('.')

    while len(b) < 2 :
        b = b + '0'
    answer = (a + '.' + b)
    print(answer)
