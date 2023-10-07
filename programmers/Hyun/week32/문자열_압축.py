def solution(s):
    def make_word(count, word):
        if count > 1:
            return str(count) + word
        return word

    def find(n, s):
        words = [s[i:i + n] for i in range(0, len(s), n)]
        zip_s = ""
        count = 0
        prev_word = ""

        for word in words:
            if prev_word == word:
                count += 1
            else:
                zip_s += make_word(count, prev_word)
                count = 1
                prev_word = word

        zip_s += make_word(count, prev_word)
        return len(zip_s)

    if len(s) == 1:
        return 1

    ans = 10000

    for i in range(1, len(s) // 2 + 1):
        ans = min(ans, find(i, s))

    return ans
