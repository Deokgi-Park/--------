import sys
# 입력 날짜
N = int(input())
# 스케줄 데이터 입력
data = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
# DP 테이블 생성 
dp = [ 0 * N for _ in range(N+1)]
# 일수 초기화
nowVal = 0
for i in range(N):
    # 현재가치와 현재일수 dp테이블 가치 비교
    nowVal = max(nowVal, dp[i])
    # 현재일수에 상담일수를 더했을때 퇴사일보다 많은 경우 pass
    if i + data[i][0] > N:
        continue
    # 상담을 받는 경우가 좋은지, 안받는 경우가 좋은지 가치 비교 후 최대 값으로 선택
    # 현재가치를 넣을 때와 상담이 끝나는 날의 가치를 비교해서 좋은 경우로 dp 테이블 입력? 그리디?
    dp[i+data[i][0]] = max(nowVal + data[i][1], dp[i+data[i][0]])
    #print(dp)
print(max(dp))
