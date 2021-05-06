class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        root = self.root
        for w in word:
            if w not in root:
                root[w] = {}
            root = root[w]
        root["#"] = word

    def search(self, word):
        children = self.root
        for i in word:
            if i not in children:
                return False
            children = children[i]

        return '#' in children

    def delete(self, word):

    def backtrack(self, start, word, root):
        if not root:
            return None
        if start == len(word):
            root.isLeaf = False
            if len(root.children) == 0:
                del root
                root = None
            return root

        if word[start] not in root.children:
            for i in root.children:
                root.children[word[start]] = self.backtrack(0, word, root.children[i])
        else:
            root.children[word[start]] = self.backtrack(start+1, word, root.children[word[start]])
        if len(root.children) == 0 and root.isLeaf == False:
            del root
            root = None

        return root

    def remove(self, root, key, depth):
        if not root:
            return None
        if depth == len(key):
            if root.isLeaf:
                root.isLeaf = True

            if len(root.children) == 0:
                del root
                root = None

            return root

        index = key[depth] - 'a'
        root.children[index] = self.remove(root.children[index], key, depth+1)
        if len(root.children) == 0 and root.isLeaf == False:
            del root
            root = None
        return root
