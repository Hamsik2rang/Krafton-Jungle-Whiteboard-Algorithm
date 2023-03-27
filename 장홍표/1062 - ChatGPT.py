import sys
from itertools import combinations

# 입력값 받아오기
N, K = map(int, sys.stdin.readline().split())
words = [sys.stdin.readline().strip() for _ in range(N)]

# K가 5보다 작거나 같으면 학생들이 읽을 수 있는 단어의 개수는 0이다.
if K <= 5:
    print(0)
else:
    # 가능한 단어의 개수를 찾기 위해 "anta"와 "tica" 사이의 글자들을 모두 추출한다.
    candidates = set()
    for word in words:
        for c in word[4:-4]:
            candidates.add(c)

    # K개의 글자를 선택하여 가능한 모든 단어를 만든다.
    max_count = 0
    for selected in combinations(candidates, K-5):
        # "anta"와 "tica"를 포함하여 단어를 만든다.
        learned = set(['a', 'n', 't', 'i', 'c'] + list(selected) + ['a', 't', 'i', 'c'])

        # 가능한 단어를 찾아서 등장하는 횟수가 가장 많은 단어의 개수를 찾는다.
        count = 0
        for word in words:
            if set(word).issubset(learned):
                count += 1
        max_count = max(max_count, count)

    # 출력
    print(max_count)