from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}  # 자식 노드들을 저장할 딕셔너리
        self.index = -1  # 현재 노드에서 끝나는 단어의 인덱스 (-1은 노드가 단어의 끝이 아님을 의미)
        self.palindrome_suffixes = []  # 현재 노드에서 끝나는 회문 단어들의 인덱스 리스트


class Trie:
    def __init__(self):
        self.root = TrieNode()  # 루트 노드 생성

    def is_palindrome(self, word):
        return word == word[::-1]  # 주어진 단어가 회문인지를 판별하는 함수

    def add_word(self, word, index):
        node = self.root
        for i, char in enumerate(reversed(word)):  # 단어를 거꾸로 순회하면서 트라이에 저장
            if self.is_palindrome(word[:len(word) - i]):  # 현재 위치부터 단어의 끝까지가 회문이라면
                node.palindrome_suffixes.append(index)  # 회문 단어 리스트에 인덱스 추가

            if char not in node.children:  # 현재 문자가 자식 노드에 없으면
                node.children[char] = TrieNode()  # 자식 노드를 만들어서 저장
            node = node.children[char]  # 현재 노드를 자식 노드로 이동

        node.index = index  # 단어의 끝에 해당하는 노드의 index에 현재 단어의 인덱스 저장

    def search_palindromes(self, word, index, result):
        node = self.root

        for i, char in enumerate(word):  # 단어를 순회하면서 회문 쌍을 찾음
            # 현재 노드에서 끝나는 다른 단어가 있고, 현재 위치부터 단어의 끝까지가 회문이면
            if node.index >= 0 and node.index != index and self.is_palindrome(word[i:]):
                result.append([index, node.index])  # 회문 쌍으로 추가

            if char not in node.children:  # 현재 문자가 자식 노드에 없으면
                return  # 더 이상 회문을 찾을 수 없으므로 종료

            node = node.children[char]  # 현재 노드를 자식 노드로 이동

        for suffix_idx in node.palindrome_suffixes:  # 현재 노드에서 끝나는 회문 단어들에 대해
            if suffix_idx != index:  # 현재 단어와 인덱스가 다르면
                result.append([index, suffix_idx])  # 회문 쌍으로 추가


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()
        for i, word in enumerate(words):  # 모든 단어를 트라이에 추가
            trie.add_word(word, i)

        result = []
        for i, word in enumerate(words):  # 모든 단어에 대해 회문 쌍을 검색
            trie.search_palindromes(word, i, result)

        return result  # 회문 쌍의 리스트를 반환
