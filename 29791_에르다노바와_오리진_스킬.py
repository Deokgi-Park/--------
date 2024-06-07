nova_skill_click, org_skill_click = map(int,input().split())

nova_click_time = set(map(int, input().split()))
org_click_time = set(map(int, input().split()))

skill_used = []

for data in nova_click_time:
    skill_used.append([data,1])

for data in org_click_time:
    skill_used.append([data,2])

skill_used.sort()

# 셋팅값
mop_gard = 90
nova_cool = 100
org_cool = 360

# 전역 상태 
nova_mop_stat = 0
org_mop_stat = 0
nova_prev_time = 0
org_prev_time = 0
nova_cool_time = 0
org_cool_time = 0

# answer 
dontmove_cnt = 0
never_dontmove_cnt = 0

def novaskill(nova_skill_click_time):
    global dontmove_cnt
    global nova_prev_time
    global nova_mop_stat
    global mop_gard
    global nova_cool_time
    if (nova_skill_click_time - nova_prev_time) >= nova_cool_time:
        nova_mop_stat -= (nova_skill_click_time - nova_prev_time)
        nova_prev_time = nova_skill_click_time
        nova_cool_time = nova_cool
        if nova_mop_stat <= 0 :
            dontmove_cnt += 1
            nova_mop_stat = mop_gard
    else :
        nova_mop_stat -= (nova_skill_click_time - nova_prev_time)

def orgskill(org_skill_click_time):
    global never_dontmove_cnt
    global org_prev_time
    global org_mop_stat
    global mop_gard
    global org_cool_time
    if (org_skill_click_time - org_prev_time) >= org_cool_time:
        org_mop_stat -= (org_skill_click_time - org_prev_time)
        org_prev_time = org_skill_click_time
        org_cool_time = org_cool
        if org_mop_stat <= 0 :
            never_dontmove_cnt += 1
            org_mop_stat = mop_gard
    else :
        org_mop_stat -= (org_skill_click_time - org_prev_time)

for skill in skill_used:
    if skill[1] == 1:
        novaskill(skill[0])
    if skill[1] == 2:
        orgskill(skill[0])

print(dontmove_cnt, never_dontmove_cnt)