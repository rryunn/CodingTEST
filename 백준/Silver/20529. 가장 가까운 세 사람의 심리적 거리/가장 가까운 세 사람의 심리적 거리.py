T = int(input())

for _ in range(T):
    n = int(input())
    mbti = input().split(' ')
    
    if n > 32:
        print(0)
        #비둘기집 원리 : n+1마리의 비둘기가 있다면 무조건 2마리이상인 집이 있다
        #마찬가지로 16가지기에 17명이면 2명은 무조건 mbti가 겹친다
        #33명이라면 무조건 3명은 mbti는 겹치기 때문에 
        #n이 32보다 크면 무조건 세 사람의 심리적 거리가 0이다.
        
    else:
    
       # MBTI 유형 간의 거리를 저장할 2차원 리스트 초기화
        distance = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(i+1, n):
                dist = 0
                for k in range(4):
                    if mbti[i][k] != mbti[j][k]:
                        dist += 1
                # 계산된 거리를 distance 배열에 저장
                distance[i][j] = distance[j][i] = dist

        ans = 10 #최대 거리가 4니까 크게 설정한거
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    ans = min(ans, distance[i][j] + distance[j][k] + distance[k][i])

        print(ans)
