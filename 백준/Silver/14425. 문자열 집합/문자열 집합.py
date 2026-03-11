import sys

input = sys.stdin.readline

n, m = map(int, input().split())

s = set()

# n번 반복
for _ in range(n):
    word = input().strip()
    s.add(word)

count = 0
# m번 반복
for _ in range(m):
    check_word = input().strip()
    if check_word in s:
        count += 1

print(count)