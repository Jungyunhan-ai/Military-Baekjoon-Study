import sys
input = sys.stdin.readline

n = int(input())
queue = []  # 1. 큐 리스트를 미리 만들어둡니다.

for _ in range(n):
    command = input().split() # 2. int()가 아닌 input() 사용

    if command[0] == "push":
        value = command[1]
        queue.append(value) # 3. 오타 수정 (queue, value)

    elif command[0] == "pop":
        if not queue: 
            print(-1)
        else:
            print(queue.pop(0))

    elif command[0] == "size":
        print(len(queue))

    elif command[0] == "empty":
        if not queue:
            print(1)
        else:
            print(0)

    elif command[0] == "front": # 4. 오타 수정 (front)
        if not queue:
            print(-1) # 끝에 콜론(:) 제거
        else:
            print(queue[0])

    elif command[0] == "back":
        if not queue:
            print(-1)
        else:
            print(queue[-1])