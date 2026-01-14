n = input()
num = n+'666'
n = int(n)
count =0
# n의 범위가 10,000보다 작으니까 다 찾아도 상관 없음.
for i in range (int(num)):
    if '666' in str(i):
        count+=1
    if count == n:
        print(str(i))
        break