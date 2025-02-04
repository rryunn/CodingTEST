day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]  # 1월 1일이 월요일이므로 0번 인덱스가 SUN

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 각 월의 일 수

x, y = map(int, input().split())

total_days = sum(month_days[:x-1]) + y  # 1월부터 (x-1)월까지의 일 수 + y일

index = total_days % 7  # 요일 계산

print(day[index])  # 결과 출력
