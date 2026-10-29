def solution(my_string, num1, num2):
    arr = list(my_string)
    a = my_string[num1]
    b = my_string[num2]
    
    arr[num1]= b
    arr[num2]=a
    return "".join(arr)

# 파이썬에서 문자열은 특정 인덱스의 문자만 직접 바꿀 수 없음.
# 문자열은 변경할 수 없는 자료형이기 때문.
# 리스트로 바꾸어서 진행할 것.