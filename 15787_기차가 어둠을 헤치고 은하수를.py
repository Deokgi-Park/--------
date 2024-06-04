import sys
N, call = map(int,input().split())
train = [0] * N

def one_call(i,x):
    train[i] |= (1<<x)
def two_call(i,x):
    train[i] &= ~(1<<x)
def three_call(i):
    train[i] = train[i] << 1
    #train[i] &= ((2**20)-1)
    if train[i] >= (2**20):
        train[i] -= (2**20)
def four_call(i):
    train[i] = train[i] >> 1
    
for i in range(call):
    data = list(map(int,sys.stdin.readline().strip().split()))
    if data[0] == 1:
        one_call(data[1]-1,data[2]-1)
    elif data[0] == 2:
        two_call(data[1]-1,data[2]-1)
    elif data[0] == 3:
        three_call(data[1]-1)
    else :
        four_call(data[1]-1)
train = set(train)
print(len(train))