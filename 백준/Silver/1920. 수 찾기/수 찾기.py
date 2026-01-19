n = int(input())
# 4 1 5 2 3 
# arr = [input().split()]
# 문자열로 출력되는거 확인
# int를 앞에 붙이려고 하자 map이 생각남
# [] 안에 map 쓰는게 어색해서 list 붙인다는게 생각남!
arr = set(map(int,input().split()))
m = int(input())
arr2 = list(map(int,input().split()))

for i in arr2:
    if i in arr: # 이렇게 되면 시간복잡도가 O(NM) 초과!
        print(1)
    else:
        print(0)
# 시간 초과 ..

#존재 여부 확인을 빠르게 하기 위해서는 리스트 대신
# SET집합이나 딕셔너리를 사용

