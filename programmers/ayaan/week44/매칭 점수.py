import collections
import re


def solution(word, pages):
    scores = collections.defaultdict(int)
    links = collections.defaultdict(int)
    to_me_link = collections.defaultdict(list)

    for page in pages:
        posl = posr = 0
        # meta 태그에서 title 찾기
        posl = page.find('<meta property="og:url" content="', posl)
        posr = page.find('"/>', posl)
        posl = page.find('https://', posl)
        title = page[posl:posr]
        scores[title] = 0
        links[title] = 0

        # body 태그 찾기
        posl = page.find('<body>')
        posr = page.find('</body>')
        body = page[posl + 6:posr]

        # body에서 word 개수 구하기
        for find in re.findall('[a-zA-Z]+', body):
            if find.upper() == word.upper():
                scores[title] += 1

        # a 링크 개수 구하기
        while True:
            posl = page.find('<a href', posl + 1)
            if posl == -1:
                break
            posr = page.find('">', posl)
            link = page[posl + 9:posr]
            links[title] += 1
            to_me_link[link].append(title)

    total_score = []
    for title in scores:
        link_score = 0
        if title in to_me_link:
            for link in to_me_link[title]:
                if links[link] == 0:
                    link_score += scores[link]
                else:
                    link_score += scores[link] / links[link]
        total_score.append(scores[title] + link_score)

    return total_score.index(max(total_score))


solution("Muzi", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"])
