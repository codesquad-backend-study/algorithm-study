import sys

sys.setrecursionlimit(10 ** 6)


def find_root(nodes):  # 현재 리스트에서 루트 노드를 찾는 메서드
    return max(nodes, key=lambda x: x[2])


def divide_nodes(nodes, y):  # 자신의 왼쪽과 오른쪽을 나누는 메서드
    for i, node in enumerate(nodes):
        if y == node[2]:
            return nodes[:i], nodes[i + 1:]


def solution(nodeinfo):
    nodes = [(i + 1, x, y) for i, (x, y) in enumerate(nodeinfo)]  # 노드의 숫자와 함께 저장
    pre_list, post_list = [], []

    def make_tree(nodes):
        if not nodes: return
        i, x, y = find_root(nodes)
        pre_list.append(i)  # inorder에 저장
        x_nodes = sorted(nodes, key=lambda x: x[1])  # x 좌표를 기준으로 정렬한 리스트
        left_nodes, right_nodes = divide_nodes(x_nodes, y)
        make_tree(left_nodes)  # 왼쪽부터
        make_tree(right_nodes)  # 오른쪽부터
        post_list.append(i)  # post order에 저장

    make_tree(nodes)

    answer = [pre_list, post_list]
    return answer

solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]])
