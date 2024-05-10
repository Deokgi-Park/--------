import sys
sys.setrecursionlimit(100000000)
N = int(input())
data = [[] for _ in range(N+1)]
visited = [False] * (N+1)
maxdis = []
while True:
    try:
        index, next, dis = map(int, sys.stdin.readline().strip().split())
        data[index].append([next,dis])
        data[next].append([index,dis])
    except:
        break

def dfs(root, dis):
    visited[root] = True
    for i in data[root] :
        if not visited[i[0]] :
            dfs(i[0], dis + i[1])
    maxdis.append([dis,root])
dfs(1, 0)
maxdis.sort(reverse=True)
visited = [False] * (N+1)
dfs(maxdis[0][1], 0)
maxdis.sort(reverse=True)
print(maxdis[0][0])