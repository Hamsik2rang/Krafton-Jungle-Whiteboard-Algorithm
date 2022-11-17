import sys

string=list(sys.stdin.readline().strip())
cursor=len(string)

# 리스트의 삭제&추가 연산 시간복잡도: O(n)
# n<100,000, m<500,000
# 최악의 경우: 100,000의 연산 500,000번 할수 있음

#---------시간초과난 코드----------------
for _ in range(int(sys.stdin.readline())):
    command=list(sys.stdin.readline().split())
    if command[0]=="L" and cursor!=0:
        # 커서를 왼쪽으로, 맨앞일 경우 무시
        cursor-=1
    elif command[0]=="D" and cursor!=len(string): 
        # 커서를 오른쪽으로, 맨 뒤일 경우 무시
        cursor+=1
    elif command[0]=="B" and cursor!=0:
        # 커서 왼쪽 문자 삭제, 맨 앞일 경우 무시
        del string[cursor-1] #
        cursor-=1
    elif command[0]=="P": 
        idx=cursor if cursor!=0 else 0
        string.insert(idx,command[1]) #
        cursor+=1
    
    # print(cursor)  
    # print(string)

print(''.join(string))