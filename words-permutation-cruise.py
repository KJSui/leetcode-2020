class Solution:
    def wordPermutation(self, words, mapwords):



    def helper(self, words, mapwords, start, idx, tmplist):
        if idx == len(words):
            return
        if start == len(mapwords[words[idx]]):
            
        if tmplist not in self.visited():
            self.visited.add(tmplist)
            self.res.append(tmplist[:])

        for i in range(start, len(mapwords[words[idx]])):
            self.helper(words, mapwords, i+1, idx, tmplist)