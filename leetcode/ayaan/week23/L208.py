class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.child = {}


class Trie:

    def __init__(self):
        self.head = Node(None)

    def insert(self, word: str) -> None:
        cur = self.head
        for char in word:
            if char not in cur.child:
                cur.child[char] = Node(char)
            cur = cur.child[char]
        cur.data = word

    def search(self, word: str) -> bool:
        cur = self.head
        for char in word:
            if char in cur.child:
                cur = cur.child[char]
            else:
                return False

        return cur.data == word

    def startsWith(self, prefix: str) -> bool:
        cur = self.head
        for char in prefix:
            if char in cur.child:
                cur = cur.child[char]
            else:
                return False
        return True
