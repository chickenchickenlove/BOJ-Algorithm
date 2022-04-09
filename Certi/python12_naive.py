import sys
from collections import defaultdict


sys.stdin = open('input.txt')
input = sys.stdin.readline

K, string = int(input()), (input().strip())
D = defaultdict(int)

for i in range(len(string) - K - 1):
    D[''.join(string[i:i+K])] +=1

print(D)






