import sys

input = sys.stdin.readline

n = int(input())

check = [0] * 10001

for _ in range(n):
    num = int(input())
    check[num] += 1 

for i in range(10001):
    if check[i] != 0:
        for _ in range(check[i]):
            print(i)
    