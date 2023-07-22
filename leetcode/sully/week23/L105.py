# Definition for a binary tree node.
import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 주어진 inorder, preorder 값으로 트리 만드는 문제
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        # preorder ALWAYS has the node first.
        # But you don't know the size of either branch.
        pre_popleft = collections.deque(preorder).popleft()

        # inorder ALWAYS has the left branch to the left of the node
        # and right branch to the right of the node.
        # So now you know the size of each branch.
        index = inorder.index(pre_popleft)
        # for x in inorder:
        #     index += 1
        #
        #     if x == pre_popleft:
        #         break

        node = TreeNode(inorder[index])

        node.left = self.buildTree(preorder, inorder[:index])
        node.right = self.buildTree(preorder, inorder[index + 1:])

        return node
