# 문자열 압축

def solution(s):

    def make_word(count, word):
        if count > 1:
            return str(count) + word
        return word

    def make_zip(target, length):
        words = [s[i:i + length] for i in range(0, len(target), length)]

        zip_result = ''
        count = 1
        previous = ''

        for word in words:
            if previous == word:
                count += 1
            else:
                zip_result += make_word(count, previous)
                count = 1
                previous = word

        zip_result += make_word(count, previous)
        return len(zip_result)

    answer = len(s)

    for i in range(1, len(s) // 2 + 1):
        answer = min(answer, make_zip(s, i))

    return answer
