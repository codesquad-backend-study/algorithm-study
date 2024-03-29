def solution(files):
    files_detail = []
    for file in files:
        head = ''
        number = ''
        end = False
        for ch in file:
            if not ch.isdigit():
                if end:
                    break
                head += ch
            else:
                end = True
                number += ch
        files_detail.append((head.lower(), int(number), file))

    files_detail.sort(key=lambda x: (x[0], x[1]))

    answer = []
    for file in files_detail:
        answer.append(file[2])
    return answer
