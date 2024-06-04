import sys

T = int(input())
from collections import deque
def make():
    N = int(input())
    data = sys.stdin.readline().strip().split()
    remake = deque()
    for char in data:
        if not remake:
            remake.append(char)
        elif remake[0] >= char :
            remake.appendleft(char)
        else :
            remake.append(char)     
    print(''.join(list(remake)))

for i in range(T):
   make() 