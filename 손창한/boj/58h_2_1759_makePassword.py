import sys
input = sys.stdin.readline

def bt(dpt, idx):
    # escape
    if dpt == l:
        # check consonant, vowel cnt
        v_cnt, c_cnt = 0, 0
        for i in range(l):
            if ret[i] in "aeiou":
                v_cnt += 1
            else:
                c_cnt += 1
        if v_cnt >= 1 and c_cnt >= 2:
            print("".join(ret))
        return
    for i in range(idx, c):
        ret.append(a[i])
        bt(dpt+1, i+1)
        ret.pop()

l, c = map(int, input().split())
a = sorted(list(input().rstrip().split())) # print in asc ord
ret = []
bt(0, 0)
