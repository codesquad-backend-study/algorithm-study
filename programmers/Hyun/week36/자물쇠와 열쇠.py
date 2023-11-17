def solution(key, lock):
    def check():
        for y in range(len(lock)):
            for x in range(len(lock)):
                if lock[y][x] != 1:
                    return False

        return True

    def rotate(key):
        for _ in range(3):
            rotate_key = [[-1] * len(key) for _ in range(len(key))]

            for y in range(len(key)):
                for x in range(len(key)):
                    rotate_key[x][len(key) - y - 1] = key[y][x]
            keys.append(rotate_key)
            key = rotate_key[:]

    def masking(y_offset, x_offset):
        for y in range(len(key)):
            for x in range(len(key)):
                if 0 <= y + y_offset < len(lock) and 0 <= x + x_offset < len(lock):
                    lock[y + y_offset][x + x_offset] += key[y][x]

    def unmasking(y_offset, x_offset):
        for y in range(len(key)):
            for x in range(len(key)):
                if 0 <= y + y_offset < len(lock) and 0 <= x + x_offset < len(lock):
                    lock[y + y_offset][x + x_offset] -= key[y][x]

    keys = [key]
    rotate(key)

    for key in keys:
        for y_offset in range(-len(key), len(lock)):
            for x_offset in range(-len(key), len(lock)):
                masking(y_offset, x_offset)
                if check():
                    return True
                unmasking(y_offset, x_offset)

    return False
