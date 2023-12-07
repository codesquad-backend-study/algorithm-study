import sys

sys.setrecursionlimit(10 ** 6)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution(nodeinfo):
    node_numbers = {tuple(pos): i + 1 for i, pos in enumerate(nodeinfo)}
    nodeinfo.sort()

    def go(arr: list):
        if not arr:
            return

        root = max(arr, key=lambda x: x[1])
        index = arr.index(root)

        node = TreeNode(node_numbers[tuple(root)])
        node.left = go(arr[:index])
        node.right = go(arr[index + 1:])

        return node

    def preorder(node):
        pre.append(node.val)
        if node.left is not None:
            preorder(node.left)
        if node.right is not None:
            preorder(node.right)

    def postorder(node):
        if node.left is not None:
            postorder(node.left)
        if node.right is not None:
            postorder(node.right)
        post.append(node.val)

    root = go(nodeinfo)

    pre = []
    preorder(root)
    post = []
    postorder(root)

    return [pre, post]
