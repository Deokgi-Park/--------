# import sys

# S, N = map(int, sys.stdin.readline().split())
# E = list(map(int,sys.stdin.readline().split()))
# K, L = map(int, sys.stdin.readline().split())
# RUN = [0]*N
# for i in range(N):
#     dis = abs(S-E[i])
#     jumpMax = dis//2
#     oddEven = dis%2
#     if oddEven == 1:
#         canJump = jumpMax-K
#         if canJump > 0 :
#             jumpMaxRest = jumpMax - canJump
#             RUN[i] +=  (jumpMaxRest*L)*2+L
#         else :
#             if jumpMax == 0:
#                 RUN[i] += L
#             else :
#                 RUN[i] += K+(jumpMax)
#     else:
#         canJump = jumpMax-K
#         if canJump > 0 :
#             jumpMaxRest = jumpMax - canJump
#             RUN[i] +=  (jumpMaxRest*2*L)
# for i in range(N):
#     if i == 0:
#        answer = [RUN[i],i+1] 
#     if answer[0] > RUN[i]:
#         answer[0] = RUN[i]
#         answer[1] = i+1

# print(answer[0], answer[1])


import sys

S, N = map(int, sys.stdin.readline().split())
E = list(map(int,sys.stdin.readline().split()))
K, L = map(int, sys.stdin.readline().split())
RUN = [0]*N
for i in range(N):
    dis = abs(S-E[i])
    if dis >= 2*K:
        RUN[i] = L*(dis-(2*K))
    else :
        RUN[i] = abs(dis-2*K)

for i in range(N):
    if i == 0:
       answer = [RUN[i],i+1] 
    if answer[0] > RUN[i]:
        answer[0] = RUN[i]
        answer[1] = i+1

print(answer[0],answer[1])


