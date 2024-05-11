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
    try:
        answer = A/B
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
    if val.count('-') == 3:
        ga1, A, ga2, B = val.split('-')
        A = int(A,8)
        B = int(B,8)        
    elif val.count('-') == 2:
        tmp1, tmp2, tmp3 = val.split('-')
        if tmp1 == '':
            A = -int(tmp2,8)
            B = int(tmp3,8)        
        if tmp2 == '':
            A = int(tmp1,8)
            B = -int(tmp3,8)        
    else:
        A, B = val.split('-')
        A = int(A,8)
        B = int(B,8)
    answer = A-B
    answer = format(answer,'o')
print(answer)