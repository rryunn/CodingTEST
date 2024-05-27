n = int(input())
dp = [0, 1]
for i in range(2, n+1):
    res= 4
    j = 1
    while (j**2) <= i:
        res = min(res, dp[i-j**2])
        j += 1
    dp.append(res + 1)
print(dp[n])