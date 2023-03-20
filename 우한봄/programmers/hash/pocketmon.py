def solution(nums):
    
    s_num=len(set(nums))
    max_num=len(nums)//2
    if s_num<max_num: 
        answer=s_num
    else:
        answer=max_num
        
    return answer