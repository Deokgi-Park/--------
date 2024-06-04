def cal(stat):
    return round(stat[0]*(1+(stat[1]/100))*((1-min(stat[2]/100,1)+min(stat[2]/100,1)*(stat[3]/100)))*(1+(stat[4]/100)))

def change(user, org_weapon, new_weapon):
    for i in range(len(user)):
        user[i] -= org_weapon[i]
    for i in range(len(user)):
        user[i] += new_weapon[i]
    return cal(user)

user1 = list(map(int,input().split()))
user2 = list(map(int,input().split()))
user_item1 = list(map(int,input().split()))
user_item2 = list(map(int,input().split()))

user1_power = cal(user1)
user2_power = cal(user2)

user1_change_power = change(user1, user_item1, user_item2)
user2_change_power = change(user2, user_item2, user_item1)


if(user1_power < user1_change_power):
    print('+')
elif(user1_power == user1_change_power):
    print('0')
else:
    print('-')

if(user2_power < user2_change_power):
    print('+')
elif(user2_power == user2_change_power):
    print('0')
else:
    print('-')