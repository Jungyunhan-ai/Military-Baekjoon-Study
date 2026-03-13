# 1. 몇 개의 숫자를 입력받을지 결정
N = int(input())

# 2. 숫자들을 담을 빈 '리스트' 만들기
numbers = []

# 3. N번만큼 반복하면서 숫자를 리스트에 추가하기
for _ in range(N):
    num = int(input())
    numbers.append(num)

# 4. 리스트 정렬하기
numbers.sort()

# 5. 정렬된 숫자들을 하나씩 꺼내서 출력하기
for n in numbers:
    print(n)