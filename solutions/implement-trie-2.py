# Implement Trie (Prefix Tree)
# All operations O(word)

class TrieNode:
    def __init__(self, val: str):
        self.val = val
        self.children = {}
        self.end = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = TrieNode('')

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.head
        i = 0
        while i < len(word) and word[i] in curr.children:
            curr = curr.children[word[i]]
            i = i + 1
        while i < len(word):
            curr.children[word[i]] = TrieNode(word[i])
            curr = curr.children[word[i]]
            i += 1
        curr.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.head
        for c in word:
            if not(c in curr.children):
                return False
            curr = curr.children[c]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.head
        for c in prefix:
            if not(c in curr.children):
                return False
            curr = curr.children[c]
        return True

# Driver Code
trie = Trie()
trie.insert('apple')
print(trie.search('apple'))
print(trie.search('app'))
print(trie.startsWith('app'))
trie.insert('app')
print(trie.search('app'))
