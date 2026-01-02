n = int(input())
nums = list(map(int,input().split()))

# 코테에서 소수 구하는 방식
# 1 이하는 소수가 아니다
# 2부터 루트 n까지 살펴봐라
# 나눠떨어지면 바로 탈락!
count =0
for i in nums:
    if i<=1:
        continue
    is_prime = True
    
    for j in range(2, int(i**0.5)+1):
        if i%j ==0:
            is_prime = False
            break
    if is_prime:
        count+=1
print(count)