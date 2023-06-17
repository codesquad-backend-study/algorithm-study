import collections


def lengthOfLongestSubstring(s: str) -> int:
    answers = []

    counter = collections.Counter(s)
    if len(counter) == len(s):
        return len(s)

    for index, start in enumerate(s):
        if index == len(s) - 1:
            break
        results = [start]
        pointer2 = index + 1
        while s[pointer2] not in results and pointer2 < len(s):
            results.append(s[pointer2])
            pointer2 += 1
            if pointer2 == len(s):
                break
        answers.append(''.join(results))

    answers.sort(key=len, reverse=True)
    print(answers[0])
    return len(answers[0])


lengthOfLongestSubstring("aab")
