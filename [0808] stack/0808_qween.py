T = int(input())

# 행 번호를 통해 재귀함수 만들 것
# 종료 조건, 재귀 호출

# r: 내가 r번째 행에 퀸을 놓을지 말지 선택하고 있음
# n = 남은 퀸의 개수
def place_queen(r, n):
    global count

    # 0. 가지치기 (선택)

    # 1. 종료조건
    if n == 0 and r == N:
        # 퀸을 n개 놓는 경우의 수 발견
        count += 1
        return
    # 2. 재귀호출
        # 내가 r번째 행에 퀸을 놓았다면 -> 다음 행 진행 가능
        # 내가 r번째 행에 퀸을 놓지 않았다면 -> 다음 행 진행 불가능(답없음)
        # 그럼 남은 행에서 최소 2개를 놔야하는데 그럼 공격해버림
    # r번째 행의 c번 열에 퀸을 놓을지 말지 생각
    for c in range(N):
        # 내가 (r,c)에 퀸을 놓을 수 있나 없나 검사
        can_place = True
        # (r,c) 위를 검사해서 퀸을 공격할 수 있는 위치에 있다면 False로 바꿈

        # 세로 검사
        # 위 방향에 퀸을 놓은 적 있나 없나 검사
        for i in range(r):
            # (i,c) 위치에 퀸이 있나 없나 검사
            if board[i][c] == 1:
                can_place = False
                break

        for i in range(1, r + 1):
            # 좌상 대각선 검사
            if r - i >= 0 and c - i >= 0 and board[r-i][c-i] == 1:
                # 좌상 대각선으로 가다가 퀸 발견 => 불가능
                can_place = False
                break

            # 우상 대각선 검사
            if r-i >=0 and c+i < N and board[r-i][c+i] == 1:
                # 우상 대각선으로 가다가 퀸 발견 => 불가능
                can_place = False
                break
        # 위쪽 검사 끝내고 다음 행으로 갈 수 있으면 재귀 호출
        if can_place:
            # r+1번째 행으로 퀸을 놓으러 가자
            board[r][c] = 1 # 현재 위치에 퀸 놓았다고 표시
            place_queen(r+1, n-1)  # 다음 행으로 퀸 놓으러 가자

            # (r,c)에서 퀸을 놓고 진행했던 상황 검사가 모두 끝나면
            # 다시 원상 복귀
            board[r][c] = 0
        # 갈 수 없으면 그냥 종료

for tc in range(1, T+1):
    # N*N 크기의 체스판에 N개의 퀸을 서로 공격하지 않는 위치에 두기
    N = int(input())

    # 배치 가능한 경우의 수
    count = 0

    # 체스 판
    board = [[0]*N for _ in range(N)]
    # board[r][c]
    place_queen(0, N)

    print(f"#{tc} {count}")