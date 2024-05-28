import math

val = input()
answer = 0
if val.count('+'):
    A, B = val.split('+')
    A = int(A,8)
    B = int(B,8)
    answer = A+B
    answer = format(answer,'o')
elif val.count('/'):
    A, B = val.split('/')
    A = int(A,8)
    B = int(B,8)
    # 0으로 나누는 경우 장애처리
    try:
        answer = A/B
        # 내림
        answer = math.floor(answer) 
        answer = int(answer)
        answer = format(answer,'o')
    except:
        answer = 'invalid'
elif val.count('*'):
    A, B = val.split('*')
    A = int(A,8)
    B = int(B,8)
    answer = A*B
    answer = format(answer,'o')
else:      
    #한값만 음수
    if val.count('-') == 2:
        tmp1, tmp2, tmp3 = val.split('-')
        # 첫값이 음수
        if tmp1 == '':
            A = -int(tmp2,8)
            B = int(tmp3,8)          
    #음수 없음
    else:
        A, B = val.split('-')
        A = int(A,8)
        B = int(B,8)
    answer = A-B
    answer = format(answer,'o')
print(answer)