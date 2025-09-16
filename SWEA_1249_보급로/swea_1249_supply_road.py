import sys
sys.stdin = open('input.txt', "r")

from heapq import heappush, heappop

def dijkstra(x, y):
    pq = [(0, x, y)]
    dists = [[inf]*N for _ in range(N)]
    dists[y][x] = 0

    while pq:
        dist, now_x, now_y = heappop(pq)

        if dists[now_y][now_x] < dist:
            continue

        for dir in range(4):
            nx = now_x + dx[dir]
            ny = now_y + dy[dir]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            new_dist = dist + arr[nx][ny]

            if dists[ny][nx] <= new_dist:
                continue

            dists[ny][nx] = new_dist
            heappush(pq, (new_dist, nx, ny))

    return dists[N-1][N-1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    inf = float('inf')
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    result = dijkstra(0,0)
    print(f"#{tc} {result}")