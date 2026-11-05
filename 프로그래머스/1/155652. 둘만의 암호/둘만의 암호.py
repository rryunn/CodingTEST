def solution(s, skip, index):
    valid_chars = [c for c in "abcdefghijklmnopqrstuvwxyz" if c not in skip]
    
    answer=''
#1. s의 알파벳을 index만큼 뒤 값으로 바꾼다.
#2. index만큼의 알파벳이 z가 되면 다시 a
#3. skip에 있는 알파벳은 제외.

    for char in s:
        new_idx = (valid_chars.index(char)+index)%len(valid_chars)
        answer+=valid_chars[new_idx]
    return answer