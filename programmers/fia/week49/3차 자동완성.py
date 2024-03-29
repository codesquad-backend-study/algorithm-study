def solution(words):
    words.sort()

    answer = 0

    for index, word in enumerate(words):
        prev_ = index - 1
        next_ = index + 1

        prev_count = 0
        if prev_ >= 0:
            prev_word = words[prev_]

            for i, char in enumerate(prev_word):
                if char == word[i]:
                    prev_count += 1
                else:
                    prev_count += 1
                    break
            else:
                prev_count += 1

        next_count = 0
        if next_ < len(words):
            next_word = words[next_]

            for i, char in enumerate(word):
                if char == next_word[i]:
                    next_count += 1
                else:
                    next_count += 1
                    break

        answer += max(prev_count, next_count)

    return answer
