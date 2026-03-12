import sys

input = sys.stdin.readline

N = int(input())

data = list(map(int,input().split()))

unique_data = sorted(set(data))

dic = {val: i for i, val in enumerate(unique_data)}

for x in data:
    print(dic[x], end = ' ')