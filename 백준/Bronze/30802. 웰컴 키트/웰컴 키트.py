# 티셔츠 사이즈 6종류 , 같은 사이즈 T장 묶음 주문 ㅏ능
# 펜은 한 종류, p자루로 묶음 ㅜ문하거나 1개 시키거나.

# 티셔츠는 남아도됨. 펜은 딱 맞춰야함.
# t 최소 몇 묶음, p자루씩 최대 몇 묶음????
# 그때 펜을 한자루씩 몇 개 주문하는지??

n = int(input())
order = list(map(int,input().split()))
t,p = map(int,input().split())

# 아그니까 t개가 1개의 묶음.
# 그러면 order를 돌면서 t보다 작거나같은지 확인 후 그렇다면 +1, 그게 아니라면
# order값 / t 하거나 %가 있다면 +1 까지 추가로. 진행. 해서. 구해.
# p의 경우는 그냥 23/7 = 3 , 23%7 = 2 니까 몫과 나머지가 정답

count =0
for i in order:
    if i !=0 and i<=t: count+=1
    elif i%t ==0: count+=i//t
    else: count+= i//t+1
print(count)
print(n//p,n%p)
