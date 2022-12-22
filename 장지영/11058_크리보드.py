import sys
input = sys.stdin.readline

N = int(input())    # max button push
 
visited = []
finalList = []

def dfs(currList) : 
    button, screen, buffer, flag = currList
    if currList not in visited : 
        visited.append(currList)
        if button == N : 
            finalList.append(screen)
            return 
    
        # 4 Buttons 
        newList = []
        for i in range(4) : 
            if i == 0 : #insert
                newList = [button + 1, screen + 1, buffer, 0]
            elif i == 1 : #flag to 1
                if screen != 0 : 
                    newList = [button + 1, screen, buffer, 1]
                else : 
                    newList = [button + 1, screen, buffer, 1]
                    visited.append(newList)
                    return
            elif i == 2 : #copy to buffer
                if flag == 1 : 
                    newList = [button + 1, screen, screen, 0]
                else : 
                    # button 횟수 낭비
                    newList = [button + 1, screen, buffer, 0]
                    # visited.append(newList)
                    # return
            else : # buffer to screen
                if buffer != 0 : 
                    newList = [button + 1, screen + buffer, buffer, 0]
                else : 
                    # button 낭비
                    newList = [button + 1, screen + buffer, buffer, 0]
                    visited.append(newList)
                    return
            
            dfs(newList)
    else :
        return
        
    
dfs([0, 0, 0, 0])   
# print(finalList)
print(max(finalList))
    