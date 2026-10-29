def solution(my_string, s, e):
    arr = my_string[s:e+1][::-1]
    return my_string[:s]+arr+my_string[e+1:]
    
    
    