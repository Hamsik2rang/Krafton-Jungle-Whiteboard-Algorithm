N = int(input())

nums =(1,2,3,5,7,9)

def dfs(strnum=""):
    if len(strnum)==N:   
        print(strnum) 
        return    

    for n in nums:    
        newnum = strnum + str(n)
        if primeNum(int(newnum)):  
            dfs(newnum)   
    return

def primeNum(num):
    if (num==1):
        return False
    for i in range(2, int(num**(0.5)) + 1):
        if num % i == 0:
            return False
    return True
  
dfs()
