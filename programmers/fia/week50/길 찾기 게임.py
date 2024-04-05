import sys

sys.setrecursionlimit(10000)


def find_root(nodes):
    return max(nodes, key=lambda x: x[1])


def divide(nodes, root_y):
    for idx, (x, y, i) in enumerate(nodes):
        if y == root_y:
            return nodes[:idx], nodes[idx + 1:]


def solution(nodeinfo):
    nodes = [[point[0], point[1], idx + 1] for idx, point in enumerate(nodeinfo)]
    pre_order = []
    post_order = []

    def make_tree(nodes):
        if not nodes:
            return

        x, y, i = find_root(nodes)
        pre_order.append(i)
        x_nodes = sorted(nodes, key=lambda x: x[0])
        left_nodes, right_nodes = divide(x_nodes, y)
        make_tree(left_nodes)
        make_tree(right_nodes)
        post_order.append(i)

    make_tree(nodes)

    return [pre_order, post_order]
