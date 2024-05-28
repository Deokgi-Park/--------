import sys
N = int(input())
data = list(map(int, sys.stdin.readline().strip().split()))
dp = []
cnt = [0, 0]
def call_org(to):
    if(to == -1):
        return
    if data.count(to) > 2:
        cnt[0] += 1
        cnt[1] += data.count(to)-1
    else :
        cnt[0] += 1
        cnt[1] += 1
    #print('arryrun:',cnt, to)
    call_org(data[to])

setdata = set(data)
for i in setdata:
    #print(i)
    cnt = [0, 0]
    call_org(i)
    cnt[0]+=(data.count(i)-1)
    #cnt[1]+=(data.count(i)-1)
    print(cnt)
    dp.append(cnt)

maxcheck = max(dp)
dp.remove(maxcheck)

answer = maxcheck[0]
for i in range(len(dp)):
    if maxcheck[0] < dp[i][1] and answer < dp[i][1] :
        answer = dp[i][1]
    

print(answer)