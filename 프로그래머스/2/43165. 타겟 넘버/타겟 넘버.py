def solution(numbers, target):

    count=0
    def dfs(start,index):
        nonlocal count
        
        #최종결과가 target이랑 같으면 count+1
        if index == len(numbers):
            if start == target:
                count+=1
            return
                
        dfs(start + numbers[index],index+1)
        dfs(start - numbers[index], index+1)
    
    dfs(0,0)
    return count