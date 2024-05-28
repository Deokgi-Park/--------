import sys

N = int(input())
porket = []
for i in range(0, 2*N, 2):
    porket.append(sys.stdin.readline().strip())
    porket.append(list(map(int,sys.stdin.readline().strip().split())))

maxrevol = [0,""]
revolsum = 0
for i in range(1, 2*N, 2):
    revol = porket[i][1]//porket[i][0]
    rest = (porket[i][1]%porket[i][0]) + (revol*2)
    while(rest//porket[i][0]>=1):
        revol += rest//porket[i][0]
        rest = rest//porket[i][0]*2 + rest%porket[i][0]
    
    revolsum += revol
    if maxrevol[0] < revol :
        maxrevol[0] = revol
        maxrevol[1] = porket[i-1]
print(revolsum)
print(maxrevol[1])