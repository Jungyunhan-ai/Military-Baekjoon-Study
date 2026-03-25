import sys

# 입력을 빠르게 받기 위해 sys.stdin.readline 사용
input = sys.stdin.readline

def solve():
    n = int(input())
    # 현재 회사에 있는 사람을 담을 집합(Set) 생성
    # 집합은 중복을 허용하지 않고 탐색/삭제가 매우 빠릅니다.
    in_office = set()

    for _ in range(n):
        name, action = input().split()
        
        if action == "enter":
            in_office.add(name)
        else:
            # leave인 경우 집합에서 제거
            in_office.discard(name)

    # 사전 순의 역순으로 정렬 (리스트로 변환 후 정렬)
    result = sorted(list(in_office), reverse=True)

    # 한 줄씩 출력
    for name in result:
        print(name)

if __name__ == "__main__":
    solve()