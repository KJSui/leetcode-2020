class Solution:
    def __init__(self):
        self.length = 0
        self.dict = defaultdict(list)

    def visitWordNNode(self, queue, visited, others_visited):
        current_word, level = queue.pop(0)
        for i in range(self.length):
            interdediate = current_word[:i] + "*" + current_word[i+1:]

            for word in self.dict[interdediate]:
                if word in others_visited:
                    return level + others_visited[word]
                if word not in visited:
                    visited[word] = level + 1
                    queue.append((word, level+1))
        return None 

    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0 

        self.length = len(beginWord)

        for word in wordList:
            for i in range(self.length):
                self.dict[word[:i]+"*"+word[i+1:]].append(word)

        queue_begin = [(beginWord, 1)]
        queue_end = [(endWord, 1)]

        visited_begin = {beginWord:1}
        visited_end = {endWord: 1}

        ans = None 

        while queue_begin and queue_end:
            ans = self.visitWordNNode(queue_begin, visited_begin, visited_end)
            if ans:
                return ans 
            ans = self.visitWordNNode(queue_end, visited_end, visited_begin)
            if ans:
                return ans 

        return 0

=======================
class Solution(object):
    def laddderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        self.wmap = defaultdict(list)
        for i in wordList:
            for j in range(len(i)):
                self.wmap[i[:j] + '*' + i[j+1:]].append(j)

        startqueue = [(startWord, 1)]
        endqueue = [(endWord, 1)]

        startvisit = {startWord: 1}
        endvisit = {endWord: 1}
        ans = -1
        while startqueue and endqueue:
            ans = self.visit(startqueue, startvisit, endvisit)
            if ans:
                return ans

            ans = self.visit(endqueue, endvisit, startvisit)
            if ans:
                return ans

        return 0


    def visit(self, queue, visited, othervisited):
        current_word, level = queue.pop(0)
        for i in range(len(current_word)):
            inter_word = current_word[:i] + "*" = current_word[i+1:]
            if inter_word in self.wmap:
                for word in self.wmap[inter_word]:
                    if word in othervisited:
                        return level + othervisited[word]
                    else:
                        visited[word] = level + 1
                        queue.append((word, level+1))
        return None