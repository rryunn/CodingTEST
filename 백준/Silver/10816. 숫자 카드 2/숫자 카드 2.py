n = int(input())
arr = list(map(int,input().split()))
m = int(input())
arr2 = list(map(int,input().split()))

#dict 이용?
# arr의 요소 하나하나를 key값, value를 다 1로 세팅해둔 후 
# 같은 key가 또 나오면 value+1 하는 방식
# (key, value) ex. (10,3)

# 그럼 나중에 key가 10인거있어요? 하면 value 출력하면 되니까

# 파이썬 dict 쓰는 법
# dct1 = {key1: value1, key2:value2 ..}
dict = {}
count=0
for i in arr:
    dict[i] = dict.get(i,0)+1

# value를 0으로 초기화하려면 어쩌지 ?
for i in arr2:
    print(dict.get(i,0), end = " ")
