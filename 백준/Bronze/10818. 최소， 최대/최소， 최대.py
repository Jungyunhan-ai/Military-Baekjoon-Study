N = int(input()) #N을 정수로 받는다

numbers = list(map(int,input().split())) 

M = max(numbers) #M은 최대값
m = min(numbers) #m은 최소값

print(m,M)