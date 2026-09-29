def solution(phone_book):

    d = {}
    for p in phone_book:
        d[p] = 1
    
    for p in phone_book:
        temp=""
        for c in p:
            temp+=c
            if temp in d and temp!=p:
                return False
    return True