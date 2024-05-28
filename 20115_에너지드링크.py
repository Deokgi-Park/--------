N = int(input())
data = list(map(int,input().split()))
data.sort()
answer = 0
for i in range(N):
    if i == N-1 :
        answer += data[i]
    else:
        answer += data[i]/2
print(answer)