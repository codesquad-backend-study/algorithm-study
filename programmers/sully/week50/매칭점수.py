from typing import List


class Page:
    def __init__(self, idx, basic_score, link_score, score):
        self.idx = idx
        self.basic_score = basic_score
        self.link_score = link_score
        self.score = score


def solution(word: str, pages: List[str]):
    word = word.lower()
    word_size = len(word)
    page_hash = dict()
    page_list = []

    for idx, s in enumerate(pages):
        s = s.lower()
        mid = -1
        lt, rt = 0, 0

        while mid == -1:
            lt = s.find('<meta', lt + 1)
            rt = s.find('>', lt)
            mid = s.find('https://', lt, rt)

        rt = s.find('\"', mid)
        url = s[mid:rt]

        lt = s.find('<body>', rt)
        basic_score = 0
        start = lt

        while True:
            start = s.find(word, start + 1)

            if start == -1:
                break

            if s[start - 1].isalpha() or s[start + word_size].isalpha():
                continue

            basic_score += 1
            start += word_size

        link_score = 0
        start = lt

        while True:
            start = s.find('<a href', start + 1)

            if start == -1:
                break

            link_score += 1

        page_hash[url] = idx
        page_list.append(Page(idx, basic_score, link_score, basic_score))

    for idx, s in enumerate(pages):
        lt, rt = 0, 0

        while True:
            lt = s.find('<a href', rt)

            if lt == -1:
                break

            lt = s.find('https://', lt)
            rt = s.find('\"', lt)
            link_url = s[lt:rt]

            if link_url in page_hash:
                current_idx = page_hash[link_url]
                page_list[current_idx].score += page_list[idx].basic_score / page_list[idx].link_score

    answer = -1
    max_score = -1

    for idx, s in enumerate(page_list):
        if max_score < s.score:
            max_score = s.score
            answer = idx

    return answer


print(solution('blind', [
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>",
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>",
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"
]))
