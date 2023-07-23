class Node:
    def __init__(self, key=None):
        self.key = key
        self.data = None
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        current = self.head

        for ch in word:
            if ch not in current.children:
                current.children[ch] = Node(ch)

            current = current.children[ch]

        current.data = word

    def search(self, word: str) -> bool:
        current = self.head

        for ch in word:
            if ch not in current.children:
                return False

            current = current.children[ch]

        if current.data:
            return True

        return False

    def startsWith(self, prefix: str) -> bool:
        current = self.head

        for ch in prefix:
            if ch not in current.children:
                return False

            current = current.children[ch]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
