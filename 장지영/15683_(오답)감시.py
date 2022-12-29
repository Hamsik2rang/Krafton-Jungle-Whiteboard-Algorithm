import sys
input = sys.stdin.readline
import copy
N, M = map(int, input().split())

room = []
cctvList = []
wallList = []
for n in range (N) : 
    room.append(list(map(int, input().split())))
    for m in range(M) : 
        this = room[n][m]
        if 0 < this < 6  : 
            cctvList.append([n, m, this])
        elif this == 6 : 
            wallList.append([n, m])
# print(room)
# print(wallList)
cctvList.sort(key=lambda x : (-x[2]))
# print(cctvList)

# =============================================================
# MAP 한개를 받아 0(사각지대)의 개수를 반환한다 
def count_zero(room) : 
    zeros = 0
    for n in range(N) : 
        for m in range(M) : 
            if (room[n][m] == 0) : 
                zeros += 1
    return zeros

# dir_check로 방향 정보를 받아 받은 MAP(room) 의 정보를 변경한다 
def activate_cctv(dir_check, room, cctv) : 
    myN, myM = cctv[0], cctv[1]
    #           동 서 남 북 
    # dir_check(0, 0, 0, 0)
    
    #동
    if dir_check[0] == 1 : 
        for m in range(myM, M) : 
            if room[myN][m] != 6 : 
                room[myN][m] = -1
            else : break
    
    # 서
    if dir_check[1] == 1 : 
        for m in range(myM, -1, -1) : 
            if room[myN][m] != 6 : 
                room[myN][m] = -1
            else : break
    
    # 남 
    if dir_check[2] == 1 : 
        for n in range(myN, N) : 
            if room[n][myM] != 6 : 
                room[n][myM] = -1
            else : break
        
    # 북 
    if dir_check[3] == 1 : 
        for n in range(myN, -1, -1) : 
            if room[n][myM] != 6 : 
                room[n][myM] = -1
            else : break

#==========================================================                
# CCTV 종류 별로 activate_cctv()로 방향정보와 MAP을 전달한다 
def cctv_5(cctv, room) : 
    activate_cctv((1, 1, 1, 1), room, cctv)
    

def cctv_4(cctv, room) : 
    activate_cctv((1, 1, 1, 0), room[0], cctv)
    activate_cctv((1, 1, 0, 1), room[1], cctv)
    activate_cctv((1, 0, 1, 1), room[2], cctv)
    activate_cctv((0, 1, 1, 1), room[3], cctv)
    
    
def cctv_3(cctv, room) : 
    activate_cctv((0, 1, 1, 0), room[0], cctv)
    activate_cctv((1, 0, 0, 1), room[1], cctv)
    activate_cctv((1, 0, 1, 0), room[2], cctv)
    activate_cctv((0, 1, 0, 1), room[3], cctv)
    
def cctv_2(cctv, room) : 
    activate_cctv((0, 0, 1, 1), room[0], cctv)
    activate_cctv((1, 1, 0, 0), room[1], cctv)
    
def cctv_1(cctv, room) : 
    activate_cctv((0, 0, 0, 1), room[0], cctv)
    activate_cctv((0, 0, 1, 0), room[1], cctv)
    activate_cctv((0, 1, 0, 0), room[2], cctv)
    activate_cctv((1, 0, 0, 0), room[3], cctv)
#=================================================================
    
for cctv in cctvList : 
    if cctv[2] == 5 : 
        cctv_5(cctv, room)
    elif cctv[2] == 4 : 
        test_room = [copy.deepcopy(room) for i in range(4)]
        cctv_4(cctv, test_room)
        result = [count_zero(test_room[0]), count_zero(test_room[1]), count_zero(test_room[2]), count_zero(test_room[3])]
        idx = result.index(min(result))
        room = test_room[idx]
        
    elif cctv[2] == 3 : 
        test_room = [copy.deepcopy(room) for i in range(4)]
        cctv_3(cctv, test_room)
        result = [count_zero(test_room[0]), count_zero(test_room[1]), count_zero(test_room[2]), count_zero(test_room[3])]
        idx = result.index(min(result))
        room = test_room[idx]
        
    elif cctv[2] == 2 : 
        test_room = [copy.deepcopy(room) for i in range(4)]
        cctv_2(cctv, test_room)
        result = [count_zero(test_room[0]), count_zero(test_room[1])]
        idx = result.index(min(result))
        room = test_room[idx]
        
    elif cctv[2] == 1 : 
        test_room = [copy.deepcopy(room) for i in range(4)]
        cctv_1(cctv, test_room)
        result = [count_zero(test_room[0]), count_zero(test_room[1]), count_zero(test_room[2]), count_zero(test_room[3])]
        idx = result.index(min(result))
        room = test_room[idx]

# print(room)
print(count_zero(room))
    