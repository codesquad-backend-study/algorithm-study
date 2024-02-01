from collections import defaultdict


def solution(word, pages):
    word = word.lower()

    urls = []
    href = defaultdict(list)
    score = [[0, 0] for _ in range(len(pages))]  # 기본 점수, 외부 링크 개수

    for index, page in enumerate(pages):
        page = page.lower()

        # 페이지의 URL 찾기
        url_start = -1
        meta_end = 0
        while url_start < 0:
            meta_start = page.find('<meta', meta_end + 1)
            meta_end = page.find('>', meta_start)

            url_start = page.find('https://', meta_start, meta_end)
        url_end = page.find('\"', url_start)
        url = page[url_start:url_end]
        urls.append(url)

        # <BODY> 내 word 등장 횟수
        basic_score = 0
        body_start = page.find('<body>', url_end + 1)
        word_end = body_start
        while True:
            word_start = page.find(word, word_end + 1)
            if word_start == -1:
                break
            if not page[word_start - 1].isalpha() and not page[word_start + len(word)].isalpha():
                basic_score += 1
            word_end = word_start + len(word)

        # 외부 링크 찾기
        link_count = 0
        start = body_start
        while True:
            start = page.find('<a href', start + 1)
            if start == -1:
                break
            link_count += 1
            link_start = page.find('https://', start)
            link_end = page.find('\"', link_start)
            link_url = page[link_start:link_end]
            href[link_url].append(index)
            start = link_end

        score[index] = [basic_score, link_count]

    answer = -1
    max_score = -1
    for index, url in enumerate(urls):
        result = score[index][0]  # 기본 점수

        for linked_page in href[url]:
            result += score[linked_page][0] / score[linked_page][1]

        if max_score < result:
            answer = index
            max_score = result

    return answer
