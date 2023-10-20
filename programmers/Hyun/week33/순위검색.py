import bisect


def solution(info, query):
    def insert(root, candidate):

        current_node = root
        for data in candidate[:-1]:
            if data not in current_node:
                current_node[data] = {}

            current_node = current_node[data]

        if "score" not in current_node:
            current_node["score"] = []

        current_node["score"].append(int(candidate[-1]))
        current_node["score"].sort()

    def find(stack, root):
        count = 0
        for lang in stack[0]:
            if lang not in root:
                continue

            for job in stack[1]:
                if job not in root[lang]:
                    continue

                for career in stack[2]:
                    if career not in root[lang][job]:
                        continue

                    for food in stack[3]:
                        if food not in root[lang][job][career]:
                            continue

                        scores = root[lang][job][career][food]["score"]
                        count += len(scores) - bisect.bisect_left(scores, stack[-1][0])

        return count

    root = {}

    for candidate in info:
        insert(root, candidate.split())

    result = []

    for each in query:
        instructions = []
        for data in each.split(' '):
            if data in ['and', ' ']:
                continue
            elif data.isdigit():
                data = int(data)
            instructions.append(data)

        query_table = [
            ['cpp', 'java', 'python'],
            ['backend', 'frontend'],
            ['junior', 'senior'],
            ['chicken', 'pizza']
        ]

        stack = []
        for idx, ins in enumerate(instructions):
            if ins == '-':
                stack.append(query_table[idx])
            else:
                stack.append([ins])

        result.append(find(stack, root))

    return result
