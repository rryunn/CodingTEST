def solution(babbling):
    arr = ["aya","ye","woo","ma"]
    result=0
    
    for word in babbling:
        # 연속된 발음이 있는지 확인
        is_repeat = False
        
        for p in arr:
            if p*2 in word:
                is_repeat=True
                break
        
        if is_repeat:
            continue
        
        for p in arr:
            word = word.replace(p," ")
            
        if word.strip() == "":
            result+=1
    return result