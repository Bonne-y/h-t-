class TrieNode:
    def __init__(self):
        self.children = {}  
        self.parent = None   
        self.is_end = False 

class Trie:
    def __init__(self):
        self.root = TrieNode()  
    
    def add(self, word): #Добавление слова в бор 
        node = self.root
        for char in word:
            if char not in node.children:
                new_node = TrieNode()
                new_node.parent = node
                node.children[char] = new_node
            node = node.children[char]
        node.is_end = True

    def _get_node(self, word): 
        node = self.root
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
    
    def search(self, word): #Поиск слова в боре
        node = self._get_node(word)
        return node is not None and node.is_end
    
    def delete(self, word):#Удаление слова из бора
        node = self._get_node(word)
        
        if not node or not node.is_end:
            return False
        
        if node.children:
            node.is_end = False
            return True
        
        while node.parent:
            parent = node.parent
            char = None
            for c, child in parent.children.items():
                if child == node:
                    char = c
                    break

            if char:  
                del parent.children[char]

            if parent.is_end or len(parent.children) > 0:
                break
                
            node = parent
        
        return True
    
