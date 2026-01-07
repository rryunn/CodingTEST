n,m = map(int,input().split())

small = min(n,m) # 아니 이것도 된다고?
#최대공약수
for i in range(small,0,-1):
    if n%i==0 and m%i==0:
        gcd = i
        break
    
#최소공배수
# while True:
#     if big%n ==0 and big%m==0:
#         lcm = big
#         break
#     big = big+1
# 시간초과엔딩
lcm = n*m//gcd

print(gcd)
print(lcm)