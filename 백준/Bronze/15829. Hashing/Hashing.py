# 항의 번호에 해당하는 만큼 특정숫자값을 거듭제곱해서 곱해준대
r = 31
M = 1234567891  
L = int(input())
word = input()
sum = 0

for i in range(L):
    n = ord(word[i])-96 #'a'는 97부터 시작하는데 우린 이게 1이 되길 바라므로
    sum += n*31**i 
print(sum%M)