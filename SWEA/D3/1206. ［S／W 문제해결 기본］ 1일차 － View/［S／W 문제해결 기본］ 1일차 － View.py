for test_case in range(1, 11):
    N = int(input())
    total = 0
    buildings = list(map(int, input().split()))
    
    for i in range(2, N - 2):
        max_neighbor = max(buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2])
        
        if buildings[i] > max_neighbor:
            total += buildings[i] - max_neighbor
            
    print(f"#{test_case} {total}")