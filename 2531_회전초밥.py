import sys
N, d, k, c = map(int, sys.stdin.readline().strip().split())
dishes = [int(sys.stdin.readline().strip()) for _ in range(N)]

maxdata = 0
    
for i in range(N):
    data = set(dishes[i:i+k])
    if i > (N-k) :
        data = data.union(set(dishes[0:i-(N-k)]))
    if len(data) >= maxdata:
        data.add(c)
        maxdata = len(data)

print(maxdata)