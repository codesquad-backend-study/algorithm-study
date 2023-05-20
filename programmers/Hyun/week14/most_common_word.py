class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall("[A-z]+", paragraph)
        words = [word.lower() for word in words]
        words = [word for word in words if word not in banned]

        counter = collections.Counter(words)
        return counter.most_common(1)[0][0]

