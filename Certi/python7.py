import sys


class Node(object) :
    def __init__(self, value):
        self.data = value
        self.next = None
        self.pre = None


class MyList(object) :
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.count = 0

    def add(self, node):
        now_node = self.head
        while now_node.next != None :
            now_node = now_node.next
        now_node.next = node
        node.pre = now_node
        self.tail = node
        self.count +=1

    def insert(self, index, node):
        cnt = 0
        now_node = self.head
        while index != cnt and now_node.next != None :
            cnt +=1
            pre_node = now_node
            now_node = now_node.next

        if self.tail == now_node :
            self.tail = node
        #
        # if now_node.data == None :
        #     now_node.next = node

        next_node = now_node.next
        now_node.next = node
        node.pre = now_node
        node.next = next_node
        self.count += 1

    def delete(self, index):
        cnt = 0
        now_node = self.head
        while index != cnt and now_node.next != None:
            cnt+=1
            pre_node = now_node
            now_node = now_node.next


        if now_node.next == None :
            self.tail = pre_node
            pre_node.next = None
        else :
            pre_node.next = now_node.next
            now_node.next.pre = pre_node
        self.count -=1

    def getTail(self):
        if self.tail :
            self.count -=1
            return_value = self.tail
            self.tail = self.tail.pre
            self.tail.next = None
            return return_value

    def getHead(self):
        if self.head.next :
            return_value = self.head.next
            if return_value.next :
                self.head.next = return_value.next
            else :
                self.head.next = None
            self.count -=1
            return return_value


    def print_index(self, index):
        cnt = 0
        now_node = self.head
        while index != cnt and now_node.next != None:
            cnt += 1
            now_node = now_node.next
        if now_node.next == None :
            print("*")
        else :
            print(now_node.next.data)



    def printAll(self):
        now_node = self.head
        while now_node.next != None:
            now_node = now_node.next
            print(now_node.data, end = " ")
        print()

def insert_func(cc,cr,string):
    note[cr].insert(cc, Node(string))
    sort_cr = cr
    while note[sort_cr].count > m :
        temp = note[sort_cr].getTail()
        note[sort_cr+1].insert(0,temp)
        sort_cr +=1

    cc += 1
    return cc, cr

def move_func(cr,cc):
    note[cr].print_index(cc)
    return cc,cr


def erase(cc,cr) :
    if cc != 0 :
        note[cr].delete(cc)
        cc -=1
        sort_cr = cr
        while note[sort_cr+1].count != 0 :
            temp = note[sort_cr+1].getHead()
            note[sort_cr].insert(9876543210, temp)
            sort_cr +=1
            if sort_cr == len(note) :
                break

    return cc, cr


n,m,q = map(int,sys.stdin.readline().split())
n = n-1
m = m-1
my_str = sys.stdin.readline().rstrip()
note = [MyList() for _ in range(n)]

row = 0
for c in my_str :
    node = Node(c)
    if note[row].count > m :
        row +=1
    note[row].add(node)

cr,cc = 0,0

for _ in range(q) :
    cmd = list(map(str,sys.stdin.readline().split()))
    if cmd[0] == 'insert':
        cc,cr = insert_func(cc,cr, cmd[1])
    elif cmd[0] == "move":
        cc,cr = move_func(*map(int,cmd[1:]))
    elif cmd[0] == "erase" :
        cc,cr = erase(cc,cr)

