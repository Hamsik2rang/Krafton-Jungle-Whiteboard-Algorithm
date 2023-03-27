'''
1. 문제의 시간 제한은?
1초
2. 문제의 최대 N값은?
알파벳 갯수26 - 기초글자5 = 21
3. 1, 2를 바탕으로 이 문제에서 허용하는 최대 시간 복잡도는?
O(N^2)
4. 3을 바탕으로 문제를 읽었을 때 사용할 수 있는 알고리즘은?
DP
5. 왜 4라고 생각했는가?
21 Combination 11을 구하면 시간초과
검사한 글자를 Visitlist로 체크하며 확인
'''

import sys
input = sys.stdin.readline

#anta~~~tica문자
#k개의 문자를 가르칠 때 학생들이 읽을수 있는 단어 최댓값
#bdefg hjklm opqrsu vwxyz
#5글자는 필수
    
def Setword():
    for i in range(N):
        wordList.append(input().strip())
        wordList[i] = list(set(wordList[i][4:-4]))
        try:
            wordList[i].remove('a')
        except:
            pass
        try:
            wordList[i].remove('c')
        except:
            pass
        try:
            wordList[i].remove('t')
        except:
            pass
        try:
            wordList[i].remove('i')
        except:
            pass
        try:
            wordList[i].remove('c')
        except:
            pass

N, K = map(int, input().strip().split())
counter = 0
wordList = []

if(K < 5):
    print("0")
elif(N==5):
    Setword()
    for i in range(len(wordList)):
        if(wordList[i] == None):
            counter += 1
else:
    N = N-5
    Setword()
    wordList.sort(key=len)
    while(N>0):
        for i in range(len(wordList)):
            # wordList[].popleft()
            pass
        
    print(wordList)
    
print(counter)