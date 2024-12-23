n = int(input())
original = n
count = 0

while True:
        
    a = n//10
    b = n%10
    new = a+b
    n = (b*10)+(new%10)

    count = count + 1

    if n == original:
        break
    
print(count)

