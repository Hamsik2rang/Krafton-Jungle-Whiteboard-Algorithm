import sys
# string=list(sys.stdin.readline())
# string=list(input())
# string=list(sys.stdin.readline().strip())
# print(string)

str_Lstack=list(sys.stdin.readline().strip())
str_Rstack=[]

for _ in range(int(sys.stdin.readline())):
    command=list(sys.stdin.readline().split())
    if command[0]=="L" and str_Lstack:
        # 커서를 왼쪽으로, 맨앞일 경우 무시
        str_Rstack.append(str_Lstack.pop())
    elif command[0]=="D" and str_Rstack: 
        # 커서를 오른쪽으로, 맨 뒤일 경우 무시
        str_Lstack.append(str_Rstack.pop())
    elif command[0]=="B" and str_Lstack:
        # 커서 왼쪽 문자 삭제, 맨 앞일 경우 무시
        str_Lstack.pop()
    elif command[0]=="P": 
        str_Lstack.append(command[1])

print(''.join(str_Lstack) + ''.join(reversed(str_Rstack)))