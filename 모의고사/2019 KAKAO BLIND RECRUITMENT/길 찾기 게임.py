# 노드들의 좌표가 담긴 배열 nodeinfo
## nodeinfo[i] = i+1번 노드의 x좌표, y좌표
# 이를 바탕으로 전위 순회, 후위 순회한 결과를 순서대로 담아 return
import sys

sys.setrecursionlimit(10000)


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def solution(nodeinfo):
    def split_node(nodes):
        if not nodes:
            return None
        val = max(nodes, key=lambda x: x[2])
        parent_idx = nodes.index(val)
        parent = Node(val[0])

        parent.left = split_node(nodes[:parent_idx])
        parent.right = split_node(nodes[parent_idx + 1:])
        return parent

    def pre_order(root, ans):
        ans.append(root.val)
        if root.left:
            pre_order(root.left, ans)
        if root.right:
            pre_order(root.right, ans)

        return ans

    def post_order(root, ans):
        if root.left:
            post_order(root.left, ans)
        if root.right:
            post_order(root.right, ans)
        ans.append(root.val)

        return ans

    nodes = []
    for idx, each in enumerate(nodeinfo):
        nodes.append((idx + 1, each[0], each[1]))

    nodes.sort(key=lambda x: x[1])
    root = split_node(nodes)

    pre_order_result = []
    pre_order(root, pre_order_result)

    post_order_result = []
    post_order(root, post_order_result)

    return [pre_order_result, post_order_result]
