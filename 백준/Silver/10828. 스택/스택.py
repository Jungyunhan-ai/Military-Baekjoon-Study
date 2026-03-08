import sys
input = sys.stdin.readline

n = int(input())
stack = [] # 변수 이름을 stack으로 통일!

for _ in range(n):
    command = input().split()

    if command[0] == "push":
        # push는 데이터를 넣는 거니까 append!
        value = command[1]
        stack.append(value)

    elif command[0] == "pop":
        if not stack:
            print(-1)
        else:
            # 스택은 맨 뒤를 빼야 하니까 pop()
            print(stack.pop())

    elif command[0] == "size":
        print(len(stack))

    elif command[0] == "empty":
        print(1 if not stack else 0)

    elif command[0] == "top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])