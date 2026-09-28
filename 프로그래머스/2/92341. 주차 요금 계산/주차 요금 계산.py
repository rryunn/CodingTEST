def solution(fees, records):
    answer = []
    #기본 시간
    com_time = fees[0]
    #기본 요금
    com_price = fees[1]
    #단위시간
    each_time = fees[2]
    #단위요금
    each_price = fees[3]
    
    check = {}
    for record in records:
        time,car, lst = record.split(" ")
        
        if car in check:
            check[car].append(time)
        
        else: check[car] = [time]

    #지금 다 문자열인거 주의
    
    for key in check:
        if len(check[key])%2==1:
            check[key].append('23:59')
            
    ans= []
    for key in check:
        arr = check[key] # 배열을 가지고 왔음
        
        for i in range(0, len(arr)-1, 2):
            in_hour, in_min = map(int,arr[i].split(":"))
            out_hour, out_min = map(int,arr[i+1].split(":"))

            cnt =0
            minute = out_min-in_min
            if minute>=0:
                cnt=(out_hour-in_hour)*60+minute
            else:
                cnt = (out_hour-in_hour-1)*60+ (60-in_min + out_min)
            ans.append((key,cnt))
            #[('5961', 145), ('5961', 1), ('0000', 34), ('0000', 300), ('0148', 670)]
        
        
    ans.sort() 
    total =0
    t = {}
    for a,b in ans:
        if a not in t:
            t[a] = b
        else:
            t[a] +=b
    
   	#{'0000': 334, '0148': 670, '5961': 146} 
    real_ans = []
    for key in t:
        value = t[key]
        if (value-com_time)%each_time!=0:
            m = (value-com_time)//each_time + 1
        else:
            m = (value-com_time)//each_time
        value = com_price +  m * each_price
        
        if(value<com_price):
            value = com_price
        real_ans.append(value)

    return real_ans