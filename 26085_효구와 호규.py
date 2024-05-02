import sys
X, Y = map(int, input().split())
data = []

zerocnt = 0
onecnt = 0

for i in range(X):
    a = list(map(int,sys.stdin.readline().strip().split()))
    zerocnt += a.count(0)
    onecnt += a.count(1)
    data.append(a)

zerocnt = zerocnt%2
onecnt = onecnt%2
visited = [[0 for _ in range(Y)] for _ in range(X)]

direction = [[0,1],[-1,0]]
# 홀수 체커
def hogu(A, B, data):
    if A or B :
        return -1
    else : 
        for i in range(X):
            for j in range(Y):
                for k in range(2):
                    if (i+direction[k][0]) >= 0 and (j+direction[k][0]) >= 0 and (i+direction[k][0]) < X and (j+direction[k][1]) < Y:
                        if data[i][j] == data[i+direction[k][0]][j+direction[k][1]]:
                            return 1
                    else: 
                        continue    
        return -1
print(hogu(zerocnt, onecnt, data))