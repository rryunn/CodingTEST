def solution(sequence, k):
    ans = []
    total =0
    stan_idx =0
    spin=0
    mx = len(sequence)-1
    while True:
        if stan_idx+spin == len(sequence):
            break
            
        total+=sequence[stan_idx+spin]
        if total==k:
            if spin <= mx :
                ans.append((stan_idx,stan_idx+spin))
                mx = spin
            total -= sequence[stan_idx]
            total -= sequence[stan_idx + spin]  # 다음 반복에서 다시 더해지므로 미리 차감
            stan_idx += 1
            spin -= 1
        elif total<k:
            spin+=1
        else:
            total-=sequence[stan_idx]
            total-=sequence[stan_idx+spin]
            stan_idx+=1
            spin-=1
            
    if len(ans)==1:
        return ans[0]
    
    ans.sort()
    for a,b in ans:
        if abs(a-b)==mx:
            return [a,b]