import sys

dct = {"Y": 0, "S": 1}
seats = [list(map(lambda x: dct[x], list(sys.stdin.readline().rstrip()))) for _ in range(5)]
count = 0
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

check = {}


def grouping(arr, depth, enemy, bit):
    if 4 <= enemy:
        return
    if depth == 7:
        global count
        count += 1
        return
    for r, c in arr:
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < 5 and 0 <= nc < 5:
                add_bit = 1 << (nr * 5 + nc)
                new_bit = bit + add_bit
                if not bit & add_bit and not check.get(new_bit, 0):
                    check[new_bit] = 1
                    grouping(arr + [(nr, nc)], depth + 1, enemy + 1 - seats[nr][nc], new_bit)


for r in range(5):
    for c in range(5):
        if seats[r][c]:
            bitmask = 1 << (r * 5 + c)
            grouping([(r, c)], 1, 0, bitmask)


print(count)
