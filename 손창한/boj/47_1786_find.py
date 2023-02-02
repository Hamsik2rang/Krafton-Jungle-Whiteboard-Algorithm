import sys
input = sys.stdin.readline

def kmp(txt, pat):
    # set skip table
    skip = [0] * (len(pat)+1)
    ps, pp = 1, 0
    skip[ps] = 0
    while ps < len(pat):
        if pat[ps] == pat[pp]:
            ps += 1
            pp += 1
            skip[ps] = pp
        elif pp == 0:
            ps += 1
            skip[ps] = pp
        else:
            pp = skip[pp]
    # str_search
    pt, pp = 0, 0
    while pt < len(txt) and pp < len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        elif pp == 0:
            pt += 1
        else:
            pp = skip[pp]
    return pt - pp if pp == len(pat) else -1

txt = input().rstrip()
pat = input().rstrip()

idx = 0
ret = []
while True:
    tmp = kmp(txt[idx:], pat)
    if tmp == -1:
        break
    ret.append(idx+tmp+1)
    idx += tmp+1
print(len(ret), *ret, sep='\n')
