class Solution:
    def findAllConcateneatedWordsInADIct(self, words):
        trie = Trie()
        result = []
        words.sort(key=len)
        memo = {}
        for i in words:
            if trie.build_and_search_trie_for_word(i, memo):
                result.append(i)
        return result

class Node(object):
    def __init__(self, val):
        self.val = val 
        self.nei = {}
        self.is_end_word = False 

class Trie:
    def __init__(self):
        self.root = Node(None)

    def build_and_search_trie_for_word(self, suffix, memo):
        current_head = self.root 
        result = False 
        for k, i in enumerate(suffix):
            if k == len(suffix)-1:
                current_head.nei[i] = Node(i)
                current_head.is_end_word = True
                continue 
            if current_head.nei.get(i) is None:
                current_head.nei[i] = Node(i)
            else:
                if current_head.nei.get(i).is_end_word and not result:
                    new_stuff = suffix[k+1::]
                    if not memo.get(new_stuff):
                        memo[new_stuff] = self.recursive_search_trie(new_stuff, self.root, self.root, memo)
                    result = memo[new_stuff]


            current_head = current_head.nei[i]
        return result 


    def recursive_search_trie(self, suffix, curr_node, root, memo):
        if len(suffix) < 1:
            reuturn True 

        result = False 
        for k, i in enumerate(suffix):
            if curr_node.nei.get(i):
                if curr_node.get(i).is_end_word:
                    new_stuff = suffix[k+1::]
                    if memo.get(new_stuff) is None:
                        memo[new_stuff] = self.recursive_search_trie(new_stuff, root, root, memo)
                    result = memo[new_stuff]
                    if result:
                        memo[suffix] = result 
                        return result 
                curr_node = curr_node.nei[i]
            else:
                break 
        memo[suffix] = result 
        return result