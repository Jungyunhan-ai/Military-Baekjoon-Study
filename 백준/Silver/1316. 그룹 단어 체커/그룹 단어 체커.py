import sys

# 1. 단어의 개수 N 입력 받기
n = int(sys.stdin.readline())
group_word_count = 0

for _ in range(n):
    word = sys.stdin.readline().strip()  # 단어 입력 (strip()으로 줄바꿈 제거)
    error = 0
    
    for index in range(len(word) - 1):  # 인덱스 0부터 마지막 앞 글자까지 확인
        # 현재 글자와 다음 글자가 다르다면? (새로운 구간 시작)
        if word[index] != word[index+1]:
            # 그런데 '다음 글자'가 '이미 나왔던 구간'에 또 있다면? (그룹 단어 아님)
            new_word = word[index+1:]  # 현재 이후의 남은 글자들만 추출
            if word[index] in new_word:
                error += 1
                break
                
    if error == 0:
        group_word_count += 1

print(group_word_count)