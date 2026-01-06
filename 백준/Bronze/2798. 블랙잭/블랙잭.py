n,m = map(int,input().split())

# 카드합이 21이 넘지 않아야한대요
# 카드합을 최대한 크게 만들어야한대요

# n장을 보이게 내려놓고 m을 외친대요
# 그럼 n장에서 3장을 골라서 
# m을 넘지않되 가장 가깝게 만들어야한대요

cards = list(map(int,input().split()))
# 하나씩 다 비교하게 되면 삼중 for문으로 시간초과가 날 것 같아요
# 아닌가 값이 그렇게 크지 않아서 괜찮으려나

max =0

length = len(cards)
for i in range(0,length):
    for j in range(i+1,length):
        for z in range(j+1,length):
            if cards[i]+cards[j]+cards[z] <= m:
                if max< cards[i]+cards[j]+cards[z] :
                    max =  cards[i]+cards[j]+cards[z] 
print(max)