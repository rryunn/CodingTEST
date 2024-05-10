T = int(input())

N = []

for i in range(T):
    N.append(int(input()))

dp = [1,1,1,2]
for i in range (4,max(N)+1):
    dp.append(dp[i-2]+dp[i-3])
    
for i in N:
    print(dp[i-1])