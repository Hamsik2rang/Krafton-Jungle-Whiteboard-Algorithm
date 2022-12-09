'''
스택에 담아 두고 뒤에서 꺼내가면서 에너지 계산
'''

n = int(input())
block = list(input())
last = ""
total = 0
jump = 0

answersheet = {
    "B":"O",
    "O":"J",
    "J":"B"
}


while(block):
    word = block.pop()
    if not block:
        # 스타트네 집
        if last==answersheet[word]:
            total+=jump*jump
        else:
            total = -1
    else:
        jump+=1
        if not last or last==answersheet[word]:
            total += jump*jump
            jump = 0
            last = word
    

print(total)