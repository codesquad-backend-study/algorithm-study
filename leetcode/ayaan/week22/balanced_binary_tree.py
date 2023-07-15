def isBalanced(root):
    answer = [True]

    def dfs(root):
        if not root:
            return 0

        left = dfs(root.left)
        right = dfs(root.right)

        if abs(left - right) > 1:
            answer[0] = False
        return max(left, right) + 1

    dfs(root)

    return answer[0]
