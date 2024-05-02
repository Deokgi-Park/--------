import sys
sys.setrecursionlimit(100000000)
N = int(input())
data = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(N)]
def recu(arr:list):
    seconde = []
    divide = len(arr)
    arrx1 = []
    arrx2 = []
    for i in range(divide):
        arrx1.append(arr[i][0:divide//2])
        arrx2.append(arr[i][divide//2:divide])
    if divide == 2:
        remake = sum(arr,[])
        remake.sort()
        remake[1]
        return remake[1]
    arr1 = arrx1[0:divide//2]
    arr2 = arrx1[divide//2:divide]
    arr3 = arrx2[0:divide//2]
    arr4 = arrx2[divide//2:divide]
    seconde.append(recu(arr1))
    seconde.append(recu(arr2))
    seconde.append(recu(arr3))
    seconde.append(recu(arr4))
    seconde.sort()
    return seconde[1]
if N == 1 :
    print(data[0][0])
else :
    answer = recu(data)
    print(answer)