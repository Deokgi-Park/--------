import sys
N = int(sys.stdin.readline().strip())
data = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(N)]

# 과제는 마감일이 가장 빠른순으로 정렬
data.sort(key = lambda data : data[1])
# 첫과제 마감일만큼 최대 딜레이 시켜보기
delay = data[0][1]
# 첫과제 미룬날짜로 초기화
answer = data[0][1] - data[0][0]

for i in range(1, N):
    # 마감일이 이전 마감딜레이와 현재 과제일수를 빼도 할수 있는지 체크
    checker = data[i][1] - data[i][0] - delay
    # 음수일 경우 마감일을 지키지 못한 것으로 음수만큼 미룬날짜(answer) 감소
    if checker < 0 :
        delay += checker + data[i][0]
        answer += checker
    else :
        delay += data[i][0]
        
print(answer)
