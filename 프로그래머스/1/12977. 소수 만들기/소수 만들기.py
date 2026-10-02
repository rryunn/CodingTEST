import math

def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(math.isqrt(n))+1):
        if n%i==0:
            return False
    return True
def solution(nums):
    n = len(nums)
    answer =0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if is_prime(nums[i]+nums[j]+nums[k]):
                    answer+=1
    return answer