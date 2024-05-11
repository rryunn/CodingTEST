N,M = map(int, input().split())

people = []
for i in range(N+M):
    people.append(input())
    
people.sort()
count = 0
results = []
for i in range(0,N+M-1):
    if people[i] == people[i+1] :
        count += 1
        results.append(people[i])
        
print(count)

for result in results:
    print(result)