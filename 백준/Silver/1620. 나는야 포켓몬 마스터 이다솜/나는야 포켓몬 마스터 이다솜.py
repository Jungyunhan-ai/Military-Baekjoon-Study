import sys
N,M = map(int, sys.stdin.readline().split()) 
# N: 포켓몬 개수, M: 맞춰야 하는 문제의 수 

name_to_id = {}
id_to_name = [""] * (N+1)
#1. 두개의 저장소 만들기
# 번호로 이름을 찾을때는 리스트 이름은 딕셔너리

for i in range(1, N+1):
    name = sys.stdin.readline().strip()
    name_to_id[name] = i
    id_to_name[i] = name

for _ in range(M):
    query = sys.stdin.readline().strip()

    if query.isdigit():
        print(id_to_name[int(query)]) #숫자로 받으면

    else:                             #문자(이름)라면 
        print(name_to_id[query])