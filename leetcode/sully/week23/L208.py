class Trie:

    def __init__(self):
        self.root = {}

    # 1. 낱말을 글자로 쪼갠 후 노드에 공통되는 글자가 있으면 그 글자 노드로 진행
    # 2. 낱말을 글자로 쪼꺤 후 노드에 그 글자가 없다면, 글자에 해당되는 노드를 만들고 진행
    def insert(self, word: str) -> None:
        current_node = self.root

        while word:
            if word[0] not in current_node:
                current_node[word[0]] = {}

            current_node = current_node[word[0]]
            word = word[1:]

        current_node[0] = {}

    def search(self, word: str) -> bool:
        current_node = self.root

        while word:
            if word[0] not in current_node:
                return False

            current_node = current_node[word[0]]
            word = word[1:]

        if 0 in current_node:
            return True

        return False

    def startsWith(self, prefix: str) -> bool:
        current_node = self.root

        while prefix:
            if prefix[0] not in current_node:
                return False

            current_node = current_node[prefix[0]]
            prefix = prefix[1:]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)