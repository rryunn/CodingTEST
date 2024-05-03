T = int(input())

N = []

for i in range(T):
    N.append(int(input()))

dp = [0,1,2,4] 
for i in range(4, max(N)+1):
    dp.append(dp[i-1]+dp[i-2]+dp[i-3]) 

for n in N:
    print(dp[n])
