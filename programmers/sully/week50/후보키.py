from itertools import combinations

def solution(relation):
    r, c = len(relation), len(relation[0])
    column_index = [i for i in range(c)]
    candidate_key = []

    for i in range(1, c+1):
        for k in list(combinations(column_index, i)):
            uniqueness = True
            chk = []

            for rel in relation:
                temp = []
                for key in k:
                    temp.append(rel[key])

                if temp in chk:
                    uniqueness = False
                    break
                else:
                    chk.append(temp)

            if uniqueness:
                current_key = ''.join(map(str, k))
                minimality = True

                for existing_key in candidate_key:
                    count = len(existing_key)
                    for ek in existing_key:
                        for ck in current_key:
                            if ek == ck:
                                count -= 1
                    if count == 0:
                        minimality = False
                        break

                if minimality:
                    candidate_key.append(current_key)
    return len(candidate_key)
