import sys
sys.setrecursionlimit(10 ** 6)
N = int(input())

answer = []
cnt = 0

def recu(line, now:list, ans):
    global cnt
    data = [0,1,2]
    if line == N:
        data.remove(0)
    
    if line == N :
        if ans != 0 and ans % 3 == 0 and len(str(ans)) == N: 
            cnt += 1
        return
    
    for i in range(len(data)):
        tmp = now[i] * (10**line)
        recu(line+1,data, ans+tmp)
    
recu(0, [0,1,2] ,0)
print(cnt)