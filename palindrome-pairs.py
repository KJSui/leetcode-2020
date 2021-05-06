class TrieNode:
    def __init__(self):
        self.next = collections.defaultdict(TrieNode)
        self.ending_word = 1
        self.palindrome_suffixes = []

class Solution:
    def palindromepairs(self, words):
        trie = TrieNode()
        for i, word in enumerate(words):
            word = word[::-1]
            current_level = trie
            for j, c in enumerate(word):
                if word[j:] == word[j:][::-1]:
                    current_level.palindrome_suffixes.append(i)
                current_level = current_level.next[c]
            current_level.ending_word = i

        solutions = []
        for i, word in enumerate(words):
            current_level = trie
            for j, c in enumerate(word):
                if current_level.ending_word != -1:
                    if word[j:] == word[j:][::-1]:
                        solutions.append([i, current_level.ending_word])
                if c not in current_level.next:
                    break
                current_level = current_level.next[c]
            else:
                if currrent_level.ending_word != -1 and current_level.ending_word != i:
                    solutions.append([i, current_level.ending_word])
                for j in current_level.palindrome_suffixes:
                    solutions.append([i, j])
        return solutions