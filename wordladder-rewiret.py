class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        self.middle = collections.defaultdict(list)
        length = len(beginWord)
        
        for word in wordList:
            for w in range(length):
                self.middle[word[:w] + '*' + word[w+1:]].append(word)
        
        startqueue = [[beginWord, 1]]
        endqueue = [[endWord, 1]]
        visited_begin = {beginWord:1}
        visited_end = {endWord:1}
        while startqueue and endqueue:
            ans = self.search(startqueue, visited_begin, visited_end)
            if ans:
                return ans
            ans = self.search(endqueue, visited_begin, visited_end)
            if ans:
                return ans
    
    def search(self, queue, begin, end):
        word, level = queue.pop(0)
        for w in range(len(word)):
            for newword in self.middle[word[:w]+'*'+word[w+1:]]:
                if newword in end:
                    return level + end[newword]
                if newowrd not in begin:
                    begin[newword] = level + 1
                    queue.append([newword, level+1])
        return None