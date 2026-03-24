import sys

# 빠른 입력을 위해 sys.stdin.readline 사용 (백엔드 코테 필수 팁)
input = sys.stdin.readline

# 1. 보드의 가로(M), 세로(N) 크기 입력 받기
N, M = map(int, input().split())

# 2. 전체 보드 상태 입력 받기 (rstrip으로 줄바꿈 문자 제거)
board = [input().rstrip() for _ in range(N)]

# 각 경우의 수마다 색칠해야 하는 개수를 저장할 리스트
repair_counts = []

# 3. 8x8 크기로 자를 수 있는 모든 시작 지점(i, j) 탐색
# 시작점 i는 0부터 N-8까지, j는 0부터 M-8까지 움직임
for i in range(N - 7):
    for j in range(M - 7):
        draw1 = 0  # 'W'로 시작하는 패턴(W-B-W-B...)으로 만들 때 필요한 페인트칠
        draw2 = 0  # 'B'로 시작하는 패턴(B-W-B-W...)으로 만들 때 필요한 페인트칠

        # 4. 시작점(i, j)부터 8x8 구역 내부를 한 칸씩 검사
        for r in range(i, i + 8):
            for c in range(j, j + 8):
                # 행(r)과 열(c)의 합이 짝수이면 시작점의 색과 같아야 하고, 홀수면 달라야 함
                if (r + c) % 2 == 0:
                    # [패턴1] 짝수 칸이 'W'여야 하는데 아니면 draw1 증가
                    if board[r][c] != 'W':
                        draw1 += 1
                    # [패턴2] 짝수 칸이 'B'여야 하는데 아니면 draw2 증가
                    if board[r][c] != 'B':
                        draw2 += 1
                else:
                    # [패턴1] 홀수 칸이 'B'여야 하는데 아니면 draw1 증가
                    if board[r][c] != 'B':
                        draw1 += 1
                    # [패턴2] 홀수 칸이 'W'여야 하는데 아니면 draw2 증가
                    if board[r][c] != 'W':
                        draw2 += 1
        
        # 5. 현재 8x8 구역에서 계산된 두 가지 패턴의 비용을 모두 저장
        repair_counts.append(draw1)
        repair_counts.append(draw2)

# 6. 저장된 모든 비용 중 가장 작은 값(최솟값)을 출력
print(min(repair_counts))