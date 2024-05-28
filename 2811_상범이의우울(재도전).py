import sys
N = int(input())
data = [0] * N
feel = list(map(int,sys.stdin.readline().strip().split()))

cnt = 0 
for i in feel:
    if i < 0:
        data[cnt] += 1 
    else:
        cnt += 1
maxdate = max(data)
maxcount = data.count(maxdate)

cnt = 0
visited = 0
save_val = 0
count = 0
answer = 0
for i in range(N):
    if feel[i] > 0:
        if visited == 0:
            cnt * 3     
        cnt = 0
    else :
        cnt += 1
    













# cnt = 0 
# for i in feel:
#     if i < 0:
#         data[cnt] += 1 
#     else:
#         cnt += 1

# T_f_minus = 0
# for i in range(N):
#     if data[i] == 0:
#         T_f_minus+=1
#     else:
#         T_f_minus -= 2*data[i]
#         if T_f_minus > 0 :
#             T_f_minus = 0
#         break


# answer = 0
# data.sort(reverse=True)
# for i in range(N):
#     if data[i] == 0:
#         break
#     elif i == 0:
#         answer += 3*data[i]
#     else :
#         answer += 2*data[i]
        
# print(answer+T_f_minus)
