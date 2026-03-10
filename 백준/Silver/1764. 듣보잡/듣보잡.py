import sys

# 1. 입력 설정
input = sys.stdin.readline

# 2. N, M 입력 받기
n, m = map(int, input().split())

# 3. 듣도 못한 사람과 보도 못한 사람을 각각 set으로 저장
# DB의 Index를 생성하는 과정과 같다.
unheard = set(input().strip() for _ in range(n))
unseen = set(input().strip() for _ in range(m))

# 4. 교집합 구하기 (Intersection)
# 두 테이블을 Join하는 것과 같은 원리
both = sorted(list(unheard & unseen))

# 5. 결과 출력
print(len(both))
for name in both:
    print(name)