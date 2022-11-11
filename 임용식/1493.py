import sys


length, width, height = map(int, sys.stdin.readline().split())
cube = [0 for _ in range(20)]
ans = 0

c = int(sys.stdin.readline())
for _ in range(c):
    a, b = map(int, sys.stdin.readline().split())
    cube[a] = b

volume = length * width * height
last_volume = 0

for i in range(c - 1, -1, -1):
    last_volume *= 2**3
    cube_size = 2**i
    max_cube_count = (length // cube_size) * (width // cube_size) * (
        height // cube_size
    ) - last_volume
    max_cube_count = min(max_cube_count, cube[i])

    ans += max_cube_count
    last_volume += max_cube_count

print(ans if last_volume == volume else -1)
