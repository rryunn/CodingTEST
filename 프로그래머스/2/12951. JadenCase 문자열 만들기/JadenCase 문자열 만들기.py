def solution(s):
    words = s.split(" ")
    res = []
    
    for word in words:
        convert = word.capitalize()
        res.append(convert)
    return " ".join(res)