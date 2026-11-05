def solution(today, terms, privacies):
    year,month,day = map(int,today.split("."))
    total = year*12*28+month*28+day
    
    ans =[]
    d = {}
    for term in terms:
        char, mon = term.split(" ")
        d[char]=int(mon)*28
            
    for i in range(len(privacies)):
        date,term = privacies[i].split(" ")
        d_year, d_month, d_day= map(int,date.split("."))
        d_total = d_year*12*28+d_month*28+d_day
            
        if d_total + d[term]<=total:
            ans.append(i+1)
    return ans