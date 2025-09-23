import sys
sys.stdin = open("input.txt", "r")

# 해당 행 경사로 가능 여부 판별 함수
def is_stair(row):
    
    # 이미 경사로 둔 경우 vistied 처리
    visited = [0]*N
    
    # 행의 인덱스를 순차로 비교
    for idx in range(len(row)-1):
        
        # 만약 같은 높이이면 계속 탐색
        if row[idx] == row[idx+1]:
            continue
        # 높이차가 2이상이면 실패
        if abs(row[idx]-row[idx+1]) > 1:
            return False
        
        # 오르막
        if row[idx] < row[idx+1]:

            # 범위 벗어남
            if idx-(L-1) < 0:
                return False
            
            # 경사로 시작지점 경사로 있는지 확인
            if visited[idx]:
                return False
            # 경사로 두기
            visited[idx] = 1
            
            for l in range(1, L):
                # 만약 이미 계단이 있으면
                if visited[idx-l]:
                    return False
                # 만약 계단 설치 도중 단차가 발생하면
                if row[idx-l] != row[idx]:
                    return False
                
                # 경사로 두기
                visited[idx-l] = 1
                
        # 내리막
        if row[idx] > row[idx+1]:
            
            # 범위 벗어남
            if idx+L >= N:
                return False
            
            # 경사로 시작지점 경사로 있는지 확인
            if visited[idx+1]:
                return False
            # 경사로 두기
            visited[idx+1] = 1
            
            for l in range(1, L):
                # 만약 이미 계단이 있으면
                if visited[idx+1+l]:
                    return False
                # 만약 계단 설치 도중 단차가 발생하면
                if row[idx+1+l] != row[idx+1]:
                    return False
                
                # 경사로 두기
                visited[idx+1+l] = 1
                
    return True           
    
N, L = map(int, input().split())

cnt = 0

# 원본 배열
arr = [list(map(int, input().split())) for _ in range(N)]

# 회전 배열 
arr_rotate = []
for i in range(N):
    row = []
    for j in range(N):
        row.append(arr[j][i])
    arr_rotate.append(row)

# 원본 배열과 회전 배열에 대해 각각 통과 가능 수 카운트
for r in arr:
    if is_stair(r):
        cnt += 1
        
for r in arr_rotate:
    if is_stair(r):
        cnt += 1
        
print(cnt)
