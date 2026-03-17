import sys

# 1. 입력 속도 최적화 (백엔드 기본 소양!)
input = sys.stdin.read

def solve():
    # 모든 데이터를 한 번에 읽어와서 공백 기준으로 나눕니다.
    data = input().split()
    
    # 첫 번째 값은 단어의 개수 N이므로 제외합니다.
    n = int(data[0])
    words = data[1:]
    
    # 2. 중복 제거 (SQL의 DISTINCT와 같은 역할)
    # set은 해시 테이블 기반이라 중복 제거가 매우 빠릅니다.
    unique_words = list(set(words))
    
    # 3. 복합 조건 정렬 (Lambda 활용)
    # 1순위: 길이(len(x)), 2순위: 알파벳 순(x)
    unique_words.sort(key=lambda x: (len(x), x))
    
    # 4. 결과 출력
    # 하나씩 print하는 것보다 join으로 한 번에 출력하는 게 성능상 유리합니다.
    sys.stdout.write('\n'.join(unique_words) + '\n')

if __name__ == "__main__":
    solve()