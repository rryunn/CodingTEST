n = int(input())

dp = [0] * 1001
dp[0] = 1
dp[1] = 3
dp[2] = 5

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp [i-2] * 2
    
print(dp[n-1] % 10007) #dp 배열 0부터 시작하니까 n-1 인덱스를 출력해야지!