# [Do it! 실습 7-2] KMP법으로 문자열 검색하기

def kmp_match(txt: str, pat: str) -> int:
    pt = 1  # txt를 따라가는 커서
    pp = 0  # pat를 따라가는 커서
    skip = [0] * (len(pat) + 1)  # 건너뛰기 표

    # 건너뛰기 표 만들기
    skip[pt] = 0
    while pt != len(pat):
        if pat[pt] == pat[pp]:
            pt += 1
            pp += 1
            skip[pt] = pp
        elif pp == 0:
            pt += 1
            skip[pt] = pp
        else:
            pp = skip[pp]

    # 검색하기
    pt = pp = 0
    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        elif pp == 0:
            pt += 1
        else:
            pp = skip[pp]

    return pt - pp if pp == len(pat) else -1

if __name__ == '__main__':
    s1 = input('text input.: \n')  # 텍스트용 문자열
    s2 = input('pat input.: \n')    # 패턴용 문자열

    idx = kmp_match(s1, s2)  # 문자열 s1~s2를 KMP법으로 검색

    if idx == -1:
        print('nopat.\n')
    else:
        print(f'{(idx + 1)} target.\n')