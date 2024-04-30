import sys 
N = int(input())
dis = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
result = 0
for i in range(1, N-1):
    beforeVal = abs(dis[i-1][0]-dis[i][0]) + abs(dis[i-1][1]-dis[i][1])
    afterVal = abs(dis[i][0]-dis[i+1][0]) + abs(dis[i][1]-dis[i+1][1])
    removeVal = abs(dis[i-1][0]-dis[i+1][0]) + abs(dis[i-1][1]-dis[i+1][1])
    goodDis = beforeVal+afterVal-removeVal
    if i == 1 : 
        checker = goodDis
        idx = i
    if checker < goodDis :
        idx = i
        checker = goodDis
dis.pop(idx)

for i in range(N-2):
    now_value = abs(dis[i][0]-dis[i+1][0]) + abs(dis[i][1]-dis[i+1][1])
    result += now_value
print(result)