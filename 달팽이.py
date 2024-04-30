import sys

N = int(input())
findData = int(input())
shell = [[0 for _ in range(N)] for _ in range(N)]
X = 0
X_MIN = 0
X_MAX = N-1
Y = 0
Y_MIN = 0
Y_MAX = N-1
start= N*N


run = 0
while(start!=0):
    shell[X][Y] = start
    if start == findData:
        save = [X+1,Y+1]
    start -= 1
    # 아래로 이동
    # 최대 값이 될때까지 이동 
    #"0 and 0"
    if X != X_MAX and Y != Y_MAX:
        X += 1
        # 최대값일때 Y의 최대값을 X에 맞춤
        if X == X_MAX:
            Y_MAX = X_MAX
    # 우측으로 이동
    # 최대 값이 될때까지 이동 
    # "0 and 1"
    elif X == X_MAX and Y != Y_MAX:
        Y += 1
    # 위로 이동
    # X 최대값을 같이 떨구면서 X최소값 까지 이동 
    # "1 and 1"
    elif X == X_MAX and Y == Y_MAX:
        X -= 1
        X_MAX -= 1
        # 최소값 도달 시 X_MAX 조건을 틀리게 수정 및 이미 사용된 MIN 값 업데이트
        if X_MIN == X:
            X_MIN += 1
            X_MAX += 1
    # 왼쪽으로 이동
    # Y 최대값을 같이 떨구면서 Y 다음 최소값(최소값+1) 까지 이동
    # 1회전 시 관 안쪽으로 이동을 구현 
    # "0 and 1"
    elif X != X_MAX and Y == Y_MAX:
        Y -= 1
        Y_MAX -= 1
        X_MAX += 1
        # 다음 최소값 도달 시 Y_MIN을 X_MIN에 맞춤 
        # Y_MAX 도 X_MAX에 맞춘 뒤 위로 이동 시 1 추가해 준 값을 X_MAX 원복하여 초기화
        if Y_MIN+1 == Y:
            Y_MIN = X_MIN
            Y_MAX = X_MAX
            X_MAX -= 1


for i in range(N):
    print(" ".join(map(str, shell[i])))
print(save[0],save[1])