import sys
sys.stdin = open("input.txt", "r")
from collections import deque

def bfs():

    while q:
        
        global answer
        answer +=1
        print(q)
        
        red_in = False
        blue_in = False
        
        red = q.pop()
        blue = q.pop()
        
        # 4방향을 탐색
        for dir in range(4):
            nx_r = red[0]+dx[dir]
            ny_r = red[1]+dy[dir]
            nx_b = blue[0]+dx[dir]
            ny_b = blue[1]+dy[dir]
            
            # 만약 길이 있으면
            if board[ny_r][nx_r] == "." or board[ny_b][nx_b] == "." or board[ny_r][nx_r] == "O" or board[ny_b][nx_b] == "O":
                print("in")
                # 끝까지 이동
                while 1:
                    # 만약 두 구슬다 앞길이 막히면 종료
                    if board[ny_r][nx_r] == "#" and board[ny_b][nx_b] == "#":
                        break
                    # 빨간 구슬이 이동 가능한 경우
                    if board[ny_r][nx_r] == "." or board[ny_r][nx_r] == "O":
                        nx_r = nx_r + dx[dir]
                        ny_r = ny_r + dy[dir]
                        if board[ny_r][nx_r] == "O":
                            red_in = True
                    # 파란 구슬이 이동 가능한 경우
                    if board[ny_b][nx_b] == "." or board[ny_b][nx_b] == "O":
                        nx_b = nx_b + dx[dir]
                        ny_b = ny_b + dy[dir]
                        if board[ny_b][nx_b] == "O":
                            blue_in =  True
                # 끝까지 이동 완료 -> 검사 실시
                
                # 만약 파란 공이 들어감 -> 다른 방향 탐색 필요
                if blue_in:
                    continue
                # 목표 달성시 종료
                if red_in:
                    return
                # 다음 방향 탐색
                q.append((nx_r, ny_r))
                q.append((nx_b, ny_b))
                        
                
                
            #     # 만약 공이 들어가면 이번 케이스는 종료
            #     if red_in or blue_in:
            #         break
            #     # 끝까지 이동완료 -> 이동 위치 정보 q에 입력
            #     q.append((nx_r, ny_r))
            #     q.append((nx_b, ny_b))
            #     break
            # # 만약 길이 없으면
            # else: 
            #     # 다음 방향 탐색
            #     continue 


N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]

# 판을 기울이면 구슬이 움직인다 -> 갈 수 있는한 최대로 이동한다.
# 구슬이 모두 같은 방향으로 동시에 움직인다
# 길이 있을 경우만 움직인다 -> 무조건 길이 있는 방향을 선택해서 기울인다.
# 빨간 구슬이 구멍에 빠져야함 # 파란 구슬이 빠지면 실패

# delta 상하좌우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

answer = 0

for y in range(N):
    for x in range(M):
        if board[y][x] == "R":
            red_bead = (x, y)
        if board[y][x] == "B":
            blue_bead = (x, y)

q = deque()
q.append(red_bead)
q.append(blue_bead)

bfs()

print(answer)





