import sys
sys.stdin = open('input.txt', "r")

from heapq import heappush, heappop

def prim(start_node):
    pq = [(0, start_node)]
    MST = [0]*N
    min_weight = 0

    while pq:
        weight, node = heappop(pq)

        if MST[node]:
            continue

        MST[node] = 1
        min_weight += weight

        for next_node in range(N):

            if MST[next_node]:
                continue

            heappush(pq, (tax_list[node][next_node], next_node))

    return(min_weight)

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = []
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    rate = float(input())

    # 인접 리스트 구현
    tax_list = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            tax = ((x[i] - x[j])**2 + (y[i]- y[j])**2)*rate
            tax_list[i].append(tax)

    result = prim(0)

    print(f"#{tc} {round(result)}")