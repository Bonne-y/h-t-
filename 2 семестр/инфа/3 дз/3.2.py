class TrieNode:
    def __init__(self):
        self.children = {} 
        self.parent = None   
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word): 
        node = self.root
        for char in word:
            if char not in node.children:
                new_node = TrieNode()
                new_node.parent = node
                node.children[char] = new_node
            node = node.children[char]
        node.is_end = True

def count(p, text):
    n = len(p)
    if n == 0 or len(text) == 0:
        return 0
    
    s = [p[i:] + p[:i] for i in range(n)]
    clear_s = list(set(s))  

    trie = Trie()
    for i in clear_s:
        trie.add(i)
    
    count = 0
    text_len = len(text)
    for i in range(text_len - n + 1):
        node = trie.root
        matched = True
        for j in range(i, i + n):
            char = text[j]
            if char not in node.children:
                matched = False
                break
            node = node.children[char]
        if matched and node.is_end:
            count += 1
    
    return count
