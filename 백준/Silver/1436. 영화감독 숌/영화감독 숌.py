import sys

input = sys.stdin.readline

N = int(input())

count = 0
target = 666

while True:
    if '666' in str(target):
        count += 1
    if count == N:
        print(target)
        break

    target += 1
    