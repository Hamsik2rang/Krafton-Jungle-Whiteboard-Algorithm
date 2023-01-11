n, d, k, c = map(int, input().rsplit()) # 벨트에 놓인 접시수,초밥종류,연속해서 먹는 접시 수, 쿠폰
arr = [int(input().rstrip()) for _ in range(n)]
lp, rp = 0, 0
answer = 0

while lp != n:
    rp = lp + k
    case = set()
    addable = True

    for i in range(lp, rp):
        i %= n
        case.add(arr[i])
        if arr[i] == c:
            addable = False

    cnt = len(case)
    if addable:
        cnt += 1
    answer = max(answer, cnt)
    lp += 1

print(answer)
