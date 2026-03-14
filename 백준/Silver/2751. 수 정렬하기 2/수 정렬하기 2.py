import sys
input = sys.stdin.readline

# 1. 몇 개의 숫자가 들어올지 입력받기
n = int(input())

# 2. 빈 리스트 만들기
numbers = []

# 3. n번 반복하면서 숫자를 입력받아 리스트에 넣기
for _ in range(n):
    num = int(input())
    numbers.append(num) # 리스트 맨 뒤에 데이터 추가

# 4. 정렬하기
numbers.sort()

# 5. 출력하기
for i in numbers:
    print(i)