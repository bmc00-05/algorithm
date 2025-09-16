import sys
sys.stdin = open('input.txt', "r")
# 숫자 선입선출 위한 덱 사용
from collections import deque

# 중복된 특정 원소가 존재 할때 순열 뽑기
def my_perm(cnt):
    global max_answer
    global min_answer

    if cnt == N-1:
        # 계산 함수에 들어갈 리스트 복사
        new_arr = pick[:]
        value = calculate(new_arr)
        # 최대 최소 갱신
        if value > max_answer:
            max_answer = value
        if value < min_answer:
            min_answer = value
        return

    for i in range(4):
        if calculator_num[i]==0:
            continue
        pick.append(i)
        # 중복 제거를 위해 입력 리스트를 이용
        calculator_num[i] -=1
        my_perm(cnt + 1)
        # 백트래킹 원상복구
        calculator_num[i] += 1
        pick.pop()

def calculate(arr):
    # 배열 복사 및 덱으로 선언
    num_copy = deque(num[:])
    # 초기 계산값 할당
    value = num_copy.popleft()
    # 연산자 pop 순서에 따라 계산
    for i in range(N-1):
        cal = arr.pop()
        if cal == 0:
            value += num_copy.popleft()
        elif cal == 1:
            value -= num_copy.popleft()
        elif cal == 2:
            value *= num_copy.popleft()
        else:
            value = int(value/num_copy.popleft())
        print(value)
    # 계산 결과 반환
    return value

T = int(input())
for tc in range(1, 1+T):

    N = int(input())
    calculator_num = list(map(int, input().split()))
    num = list(map(int, input().split()))

    # 0, 1, 2, 3 = +, -, *, /
    calculator = []
    pick = []

    max_answer = -9999999999
    min_answer = 9999999999

    for i in range(4):
        calculator += [i]*calculator_num[i]

    my_perm(0)

    print(f"#{tc} {abs(max_answer-min_answer)}")
