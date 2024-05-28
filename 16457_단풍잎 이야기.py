from itertools import combinations
n, m, k = map(int,input().split())

qs = []
# allset = set({})
for i in range(m): 
    s = set([int(x) for x in input().split()])
    # allset.update(s)
    qs.append(s)
    
comb = list(combinations(list(range(1,2*n+1)), n))

dp = [0] * len(comb)

for i, data in enumerate(comb):
    setdata = set(data)
    # if allset >= setdata:
    for j in qs:
        if setdata >= j:
            dp[i] += 1
print(max(dp))
