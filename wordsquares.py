class Solution:
    def wordSquare(self, words):
        trie = defaultdict(list)
        for word in words:
            for i in word:
                prefix = word[:i+1]
                trie[prefix].append(word)

        for word in words:
            square = [word]
            self.findCandidate(trie, square)
        
        return self.squares

    def findCandidate(self, trie, square):
        size = len(square)
        if size == len(word):
            self.squares.append(square)
            return
        prefix = ""
        for word in square:
            prefix += word[size]
        if prefix not in trie:
            return
        for candidate in trie[prefix]:
            self.findCandidate(trie, square+[candidate])
