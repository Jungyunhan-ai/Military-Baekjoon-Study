import sys

T = int(sys.stdin.readline())

for _ in range(T):
    vps = sys.stdin.readline().strip()
    stack = []
    is_vps = True                   #에러가 나는지 안나는지 확인            

    for char in vps:
        if char == '(':               #열린 괄호가 나오면 스택에 넣기
            stack.append(char)
        else: 
            if not stack:
                is_vps = False         #짝이 안맞게 나온다면 Fasle break 하기
                break
            else:
                stack.pop()            # 짝이 맞는다면 닫힌 괄호를 빼서 쓰기  

    if is_vps and not stack:           #모든 열린,닫힌 괄호가 짝이 맞았고 
        print("YES")                   #스택이 다 비어있다면 YES 아니면 NO
    else:
        print("NO")