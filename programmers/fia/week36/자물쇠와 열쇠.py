def solution(key, lock):
    def check():
        for row in range(len(lock)):
            for column in range(len(lock)):
                if lock[row][column] != 1:
                    return False

        return True

    def rotate(key):
        keys = [key]

        for _ in range(3):
            turned = [[] for _ in range(len(key))]

            for i in range(len(key)):
                for j in range(len(key) - 1, -1, -1):
                    turned[i].append(keys[-1][j][i])

            keys.append(turned)

        return keys

    def mask(r_offset, c_offset):
        for row in range(len(key)):
            for column in range(len(key)):
                if 0 <= row + r_offset < len(lock) and 0 <= column + c_offset < len(lock):
                    lock[row + r_offset][column + c_offset] += key[row][column]

    def unmask(r_offset, c_offset):
        for row in range(len(key)):
            for column in range(len(key)):
                if 0 <= row + r_offset < len(lock) and 0 <= column + c_offset < len(lock):
                    lock[row + r_offset][column + c_offset] -= key[row][column]

    turned_keys = rotate(key)

    for key in turned_keys:
        for r_offset in range(-len(key), len(lock)):
            for c_offset in range(-len(key), len(lock)):
                mask(r_offset, c_offset)
                if check():
                    return True
                unmask(r_offset, c_offset)

    return False
