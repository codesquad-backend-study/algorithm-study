import re

def solution(files):
    tmp = []

    for idx, file in enumerate(files):
        m = re.search(r'[0-9]+', file)

        head = file[:m.start()].lower()
        number = int(file[m.start():m.end()])

        tmp.append((head, number, idx))

    sorted_list = sorted(tmp, key=lambda x : (x[0], x[1]))

    ans = []
    for _, _, idx in sorted_list:
        ans.append(files[idx])

    return ans