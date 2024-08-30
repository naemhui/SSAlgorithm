'''
7
3 5 1 2 7 4 -5
'''

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None   # 관리할 데이터는 최상의 root

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)  # 없다면 그냥 삽입
        else:
            self._insert(self.root, key)  # 자리를 찾아서 삽입

    def _insert(self, node, key):
        if key < node.key:  # 작으면 왼쪽을 고려
            if node.left is None:  # 왼쪽에 삽입 가능 -> 그냥 삽입
                node.left = Node(key)
            else:
                self._insert(node.left, key)  # 왼쪽에 데이터가 있다 -> 재귀로 한 번 더 탐색
        else:
            if node.right is None:  # 넣을 수 있으면 삽입
                node.right = Node(key)
            else:
                self._insert(node.right, key)  # 못넣으면 한 번 더 들어가기

    ##3
    def delete(self, key):
        # 루트부터 삭제할지 말지 판단
        # 만약 삭제가 되었다면 다른 노드로 대체 되었을 것
        self.root = self._delete(self.root, key)


    def _delete(self, node, key):
        # 삭제 결과 그 자리에 있어야 할 노드를 리턴!!

        # 노드가 없으면 삭제x
        if node is None:
            return node

        # 현재 노드가 삭제 대상인지 판별
        # key값과 비교해서
        # key < 현재 노드 : 현재 노드의 왼쪽으로 다시 탐색
        if key < node.key:
            # 현재 노드의 왼쪽을 삭제할지 말지 판단
            # 왼쪽 노드가 삭제된다면 다른 노드로 대체
            node.left = self._delete(node.left, key)

        elif key > node.key:
            # key > 현재 노드: 현재 노드의 오른쪽으로 다시 탐색
            # 현재 노드의 오른쪽을 삭제할지 말지 판단
            # 오른쪽 노드가 삭제된다면 다른 노드로 대체
            node.right = self._delete(node.right, key)
        # key == 현재노드 : 삭제 진행
        else:
            # 1. 자식이 없는 단말 노드
            if node.left is None and node.right is None:
                # 그냥 삭제
                node = None
            # 2. 자식이 하나만 있는 경우(왼쪽 or 오른쪽)
            elif node.left is None:
                # 오른쪽 자식만 있는 경우
                node = node.right
            elif node.right is None:
                # 왼ㅉㄱ 자식만 있는 경우: 그냥 왼쪽 자식 땡겨오기
                node = node.left
            # 3. 자식이 둘 다 있는 경우
            else:
                # 1. 왼쪽 서브트리에서 최댓값
                # 2. 오른쪽 서브트리에서 최솟값
                min_node_from_right = self.get_min(node.right)
                node.key = min_node_from_right.key

                # 내가 찾은 최소 노드를 여기 위치로 땡겨온다는 건
                # 그 최소 노드가 원래 있던 자리도 누군가 대체 (삭제)
                # 오른쪽 노드부터 찾기 시작
                node.right = self._delete(node.right, min_node_from_right)

        # 마지막으로 삭제 후의 node 자리는 누군가로 대체되었음 -> return
        return node

    def _get_min(self, node):
        while node.left is not None:
            # 계속 왼쪽 자식으로 이동
            node = node.left
        # 마지막 왼쪽 자식이 최솟값
        return node


    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:  # none이거나 탐색 성공했다면
            return node
        if key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def inorder_traversal(self):
        self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        if node:
            self._inorder_traversal(node.left)
            print(node.key, end=' ')
            self._inorder_traversal(node.right)

N = int(input())
arr = list(map(int, input().split()))

bst = BinarySearchTree()

for num in arr:
    bst.insert(num)

print("중위 순회 결과:", end=' ')
bst.inorder_traversal()  # 중위 순회: -5 1 2 3 4 5 7

# 탐색 예제
key = 5
result = bst.search(key)
if result:
    print(f"\n키 {key} 찾음.")
else:
    print(f"\n키 {key} 못 찾음.")