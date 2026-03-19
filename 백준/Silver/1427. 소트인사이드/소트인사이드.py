import sys

n_list = list(sys.stdin.readline().strip())

n_list.sort(reverse=True)

print("".join(n_list))