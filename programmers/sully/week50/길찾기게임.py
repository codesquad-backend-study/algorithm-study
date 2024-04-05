class Node:
    def __init__(self, x, y, index):
        self.x = x
        self.y = y
        self.index = index
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.pre_answer = []
        self.post_answer = []

    def insert(self, parent, current):
        if parent is None:
            parent = current

        if current.x < parent.x:
            parent.left = self.insert(parent.left, current)
        elif current.x > parent.x:
            parent.right = self.insert(parent.right, current)

        return parent

    def create(self, node_list):
        for node in node_list:
            self.root = self.insert(self.root, node)

    def preorder(self, current):
        if current:
            self.pre_answer.append(current.index)
            self.preorder(current.left)
            self.preorder(current.right)

    def postorder(self, current):
        if current:
            self.postorder(current.left)
            self.postorder(current.right)
            self.post_answer.append(current.index)


def solution(node_info):
    answer = [[], []]
    new_node_info = []

    for i in range(len(node_info)):
        current_x, current_y = node_info[i]
        new_node_info.append([current_x, current_y, i + 1])

    new_node_info.sort(key=lambda x: (-x[1], x[0]))

    node_list = [Node(x[0], x[1], x[2]) for x in new_node_info]

    binary_tree = BinaryTree()
    binary_tree.create(node_list)
    binary_tree.preorder(binary_tree.root)
    binary_tree.postorder(binary_tree.root)

    for i in range(len(binary_tree.pre_answer)):
        answer[0].append(binary_tree.pre_answer[i])
        answer[1].append(binary_tree.post_answer[i])

    return answer
