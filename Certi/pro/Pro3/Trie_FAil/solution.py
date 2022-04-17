from collections import defaultdict


class Node(object):
    def __init__(self,myStr):
        self.nodeStr = myStr
        self.cnt = 0
        self.endCnt = 0
        self.child = {}

class Trie(object):

    def __init__(self):
        self.root = Node(None)

    def add_node(self,MyStr):
        cur = self.root
        cur.cnt +=1

        for c in MyStr :
            if c not in cur.child:
                cur.child[c] = Node(c)
            cur = cur.child[c]
            cur.cnt += 1
        cur.endCnt +=1

    def remove_node(self, MyStr):
        cur = self.root
        cur.cnt -=1

        for c in MyStr :
            cur = cur.child[c]
            cur.cnt -=1

        cur.endCnt -=1


    def correctWord(self, String):
        cur = self.root
        myString = [c for c in String]
        succ, deltaIdx, deltaString, deltaValue = self.dfs(0,cur,0,myString, -1,"")
        return succ, deltaIdx, deltaString

    def dfs(self, delta, node, idx, myString, deltaIdx, deltaString):
        if delta <= 1 and node.endCnt >= 1 and idx == len(myString) : return True, deltaIdx, deltaString, delta

        V = defaultdict(int)
        for nextNodeKey in sorted(node.child.keys()):
            nextNode = node.child[nextNodeKey]
            if V[nextNode] : continue
            if (delta == 1 and myString[idx] == nextNode.nodeStr) or (delta == 0) :
                next_delta = delta
                if myString[idx] != nextNode.nodeStr :
                    next_delta +=1
                    deltaIdx = idx
                    deltaString = nextNodeKey
                V[nextNode] = 1

                suc, rdeltaIdx, rdeltaString, rdeltaValue = self.dfs(next_delta, nextNode, idx+1,myString, deltaIdx, deltaString)
                if suc : return suc, rdeltaIdx, rdeltaString, rdeltaValue
                if myString[idx] != nextNode.nodeStr :
                    next_delta -=1
                    deltaIdx = -1
                    deltaString = ""
        return False, "", "", -1



my_Trie = Trie()
my_String = ''
final_str= ""
my_String_list = []


def init(N: int, stri: list) -> None:
    global my_String_list, my_String, my_Trie
    my_String_list = []
    my_String = ""
    my_Trie = Trie()
    my_String = ''.join(map(str, stri))
    my_String_list =  stri


def addDict(word: list) -> None:
    global my_String_list, my_String
    my_Trie.add_node(''.join(map(str, word)))

def removeDict(word: list) -> None:
    global my_String_list, my_String
    my_Trie.remove_node(''.join(map(str, word)))

def correctWord(start: int, end: int) -> int:
    global my_String_list, my_String
    cnt = 0
    temp_string = []
    for idx in range(start, end+1) :
        if my_String_list[idx] == "_" :
            succ, *ret = my_Trie.correctWord(''.join(map(str, temp_string)))
            if succ :
                modified(idx, ret, temp_string)
                cnt +=1
            temp_string = []
        else :
            temp_string.append(my_String_list[idx])
            if idx == end :
                succ, *ret = my_Trie.correctWord(''.join(map(str, temp_string)))
                if succ:
                    modified(idx+1, ret, temp_string)
                    cnt += 1
    return cnt


def modified(cnt, ret,temp_string) :
    global my_String_list, my_String
    deltaIdx, deltaString = ret
    if deltaIdx != "" :
        fix = cnt - len(temp_string) + deltaIdx
        my_String_list[fix] = deltaString



def destroy(result: list) -> None:
    global my_String_list, my_String
    result[:] = my_String_list
    return result

