class Page:
    def __init__(self, idx, basic, link, score):
        self.idx = idx
        self.basic = basic
        self.link = link
        self.score = score


def solution(word, pages):
    wsize = len(word)
    pagehash = {}
    pagelist = []
    word = word.lower()
    for idx, s in enumerate(pages):
        s = s.lower()
        mid = -1
        posl = posr = 0
        while mid < 0:
            posl = s.find('<meta', posl + 1)
            posr = s.find('>', posl)
            mid = s.find('https://', posl, posr)
        posr = s.find('\"', mid, posr)
        url = s[mid:posr]  # 내 이름찾기

        posl = s.find('<body>', posr)
        basic = 0
        start = posl
        while True:  # 검색어 찾기 (기본 점수)
            start = s.find(word, start + 1)
            if start == -1:
                break
            if not s[start - 1].isalpha() and not s[start + wsize].isalpha():
                basic += 1  # 기본점수 증가
                start += wsize

        link = 0
        start = posl
        while True:  # 외부 링크 개수 찾기
            start = s.find('<a href', start + 1)
            if start == -1:
                break
            link += 1  # 외부 링크 개수 증가

        pagehash[url] = idx  # 페이지 이름(링크) : 페이지 인덱스
        pagelist.append(Page(idx, basic, link, basic))

    for i, s in enumerate(pages):  # 들어오는 링크 점수 더하기
        posl = posr = 0
        while True:
            posl = s.find('<a href', posr)
            if posl == -1:
                break
            posl = s.find('https://', posl)
            posr = s.find('\"', posl)
            linkurl = s[posl:posr]
            if linkurl in pagehash:
                idx = pagehash[linkurl]
                pagelist[idx].score += pagelist[i].basic / pagelist[i].link

    ans = -1
    max_score = -1
    for idx, page in enumerate(pagelist):
        if max_score < page.score:
            max_score = page.score
            ans = idx
    return ans
