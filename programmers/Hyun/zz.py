import re
from itertools import combinations

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]

banned_id = sorted(banned_id, key=lambda x: x.count('*'))

banned_id = [id.replace('*', '.') for id in banned_id]

print(banned_id)
# for ban_id in banned_id:
#     cnt = 0
#     for use_id in user_id:
#         if re.fullmatch(ban_id, use_id) is not None:
#             cnt += 1
#
#     cnts.append(cnt)

cnt = 0
for combi in list(combinations(user_id, len(banned_id))):
    print(combi, end=" ")
    combi = list(combi)
    tmp = combi[:]
    for ban_id in banned_id:
        for id in combi:
            if re.fullmatch(ban_id, id) is not None:
                combi.remove(id)
                break

    if not combi:
        print(tmp)
        cnt += 1

    print()
print(cnt)





