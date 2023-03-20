def solution(participant, completion):
    dic_p={elm:0 for elm in participant}
    for p in participant:
        dic_p[p]+=1
    for c in completion:
        dic_p[c]-=1

    a_list=[k for k, v in dic_p.items() if v !=0]
    answer=a_list[0]
    return answer