import sys

infos = list(map(int, sys.stdin.readline().split()))

# 2의 0제곱부터 19제곱까지 (0 ≤ i < 20)
needs = [0] * 20
holds = [0] * 20
for _ in range(int(sys.stdin.readline())):
    idx, num = map(int, sys.stdin.readline().split())
    holds[idx] = num  # 보유중인 큐브 개수 입력


def PutBigCube(arr, max_size=20):  # 최소의 경우 도출
    mn, md, mx = sorted(arr)
    big = 21
    for size in range(max_size, -1, -1):  # 넣을 수 있는 최대 크기의 큐브 찾기
        if 2**size <= mn:
            big = size
            break

    cube = 2**big  # 큐브 한 변의 길이
    mn_cube, md_cube, mx_cube = 1, md // cube, mx // cube
    res_mn, res_md, res_mx = mn % cube, md % cube, mx % cube
    needs[big] += mn_cube * md_cube * mx_cube  # 가능한 가장 큰 큐브를 넣을 수 있는 만큼 집어 넣음

    # 사용할 수 있는 최대 크기의 큐브를 가능한 많이 사용하는 함수를 남은 길이에 대해 재귀적으로 실행
    if res_mx:
        PutBigCube([mn, md, res_mx], big - 1)
    if res_md:
        PutBigCube([mn, res_md, mx - res_mx], big - 1)
    if res_mn:
        PutBigCube([res_mn, md - res_md, mx - res_mx], big - 1)


PutBigCube(infos)
# 편의상 뒤집음
needs = needs[::-1]
holds = holds[::-1]

used_cube = 0
for i in range(20):
    if needs[i] <= holds[i]:
        used_cube += needs[i]
    else:
        if i == 19:
            used_cube = -1
            break
        used_cube += holds[i]
        needs[i + 1] += (needs[i] - holds[i]) * 8

print(used_cube)
