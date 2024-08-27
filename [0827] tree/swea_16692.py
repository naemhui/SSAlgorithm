N = int(input())

# 인덱스가 부모 노드의 번호인 배열 두개 준비
cleft = [0] * (N + 1)  # cleft[1] ==> 1번노드의 왼쪽 자식 노드 번호
cright = [0] * (N + 1)  # cright[1] ==> 1번노드의 오른쪽 자식 노드 번호

for i in range(N-1):

    # parent 노드의 왼쪽이 비었으면 왼쪽부터
    if cleft[parent] == 0:
        cleft[parent] = child
        
    # 왼쪽에 누가 있으면 오른쪽으로
    else:
        cright[parent] = child

# 2. 중위순회 inorder L - V - R
def inorder(t):
    # 현재 노드 번호가 t 일때
    # t번 노드가 존재 하는가?
    if t:
        # 왼쪽
        inorder(cleft[t])
        # t번 노드 방문 처리
        print(t, end=" ")
        ####################
        # 오른쪽
        inorder(cright[t])

inorder(1)
print()