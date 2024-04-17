# 기본점수, 외부링크수, 링크점수, 매칭점수

# 기본점수 => 텍스트 중 검색어가 등장하는 횟수 (대소문자 무시)
# 외부링크 수 => 해당 웹페이지에서 다른 외부 페이지로 연결된 링크 개수
# 링크점수 => 해당 웹페이지로 들어오는 다른 웹페이지의 기본점수 /  외부링크수 의 총합
# 매칭점수 => 기본점수 + 링크점수

# 검색어 word, 웹페이지 HTML 목록인 pages 가 주어짐
# 매칭점수가 가장 높은 웹페이지 index 를 구하라
## 여러개라면 번호가 가장 작은것

## meta tag => 이 웹페이지의 url
## a href => 외부링크 URL
## 모든 url 은 https:// 로만 시작

# 검색어는 완전히 단어가 일치해야 한다. => 연속, 포함 불가
# 이메일같이 골뱅이로 분류되는건 두개의 단어로 인정한다.
import re


def find_page_url(head):
    pattern = r'<meta property="og:url" content="([^"]+)"'
    url = re.search(pattern, head).group(1).strip()
    return url


def calculate_match_word(html, word):
    word = word.lower()
    words = re.split(r'[^a-z]', html.lower())
    cnt = 0
    for w in words:
        if word == w:
            cnt += 1
    return cnt


def find_externel_link(html, page_info, current_title):
    pattern = r'<a href="([^"]+)"'
    external_links = re.findall(pattern, html)
    page_info[current_title][-1] = external_links


def calculate_score(page_info):
    for title in page_info.keys():
        for externel_link in page_info[title][-1]:
            link_score = 0
            if externel_link in page_info:
                link_score += page_info[title][2] / len(page_info[title][-1])
                page_info[externel_link][0] += link_score

        page_info[title][0] += page_info[title][2]


def solution(word, pages):
    page_info = {}  # 페이지 url = [매칭점수, 인덱스, 기본점수, 외부링크]
    page_title = []
    for idx, page in enumerate(pages):
        match_cnt = calculate_match_word(page, word)
        head, _ = page.split('</head>')
        title = find_page_url(head)
        page_title.append(title)
        page_info[title] = [0, idx, match_cnt, []]

    for idx, page in enumerate(pages):
        find_externel_link(page, page_info, page_title[idx])

    calculate_score(page_info)

    return sorted(page_info.values(), key=lambda x: (-x[0], x[1]))[0][1]
