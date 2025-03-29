class Trie:

    def __init__(self) -> None:
        self.children = {}
        self.isEnd = True
    

    def insert(self, word: str) -> None:
        node = self

        for char in word:
            if char not in node.children:
                node.children[char] = Trie()
            node = node.children[char]
        node.isEnd = True
    
    def _findNode(self, word: str) -> Self:
        node = self
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def search(self, word: str) -> bool:
        node = self._findNode(word)
        return node is not None and node.isEnd
    
    def startsWith(self, prefix: str) -> bool:
        return self._findNode(prefix) is not None