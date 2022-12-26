import collections


def bfs():
    q = collections.deque()
    q.append([S, ''])
    if S == 0 or S == 1:
        V[S] = 1
    while q:
        cur_v, comm = q.popleft()
        if cur_v == T:
            return comm
        if 0 <= cur_v ** 2 <= 10 ** 9 and cur_v ** 2 and cur_v ** 2 != 1:
            q.append([cur_v ** 2, comm + '*'])
        if 0 <= 2 * cur_v <= 10 ** 9 and cur_v ** 2 and 2 * cur_v != 1:
            q.append([2 * cur_v, comm + '+'])
        if not V[0]:
            q.append([0, comm + '-'])
            V[0] = 1
        if not V[1]:
            q.append([1, comm + '/'])
            V[1] = 1
    return -1


S, T = map(int, input().split())
if S == T:
    print(0)
else:
    V = [0, 0]
    print(bfs())