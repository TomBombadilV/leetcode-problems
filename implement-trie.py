# Implement Trie (Prefix Tree)

from collections import defaultdict

class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = defaultdict(str)
        self.isEnd = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = TrieNode(None)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        print("Inserting '{0}'".format(word))
        curr = self.head
        i = 0
        # While the current letter exists in this chain, get the next letter and node
        while i < len(word) and word[i] in curr.children:
            curr = curr.children[word[i]]
            # If this is last letter in word, set node as end node
            if i == len(word) - 1:
                curr.isEnd = True
            i += 1
        # Add the rest of the letters in the word that aren't in the chain
        while i < len(word):
            # Create new node for this letter
            new = TrieNode(word[i])
            # If this is last letter in word, set node as end node
            if i == len(word) - 1:
                new.isEnd = True
            # Add new node to current node's dictionary
            curr.children[word[i]] = new
            curr = new
            # Get next letter
            i+=1

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.head
        for i in range(len(word)):
            if not(word[i] in curr.children):
                print("'{0}' isn't in trie".format(word))
                return False
            curr = curr.children[word[i]]
            if i == len(word) - 1:
                if not(curr.isEnd):
                    print("'{0}' isn't in trie".format(word))
                    return False
        print("'{0}' is in trie".format(word))
        return True

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.head
        for l in prefix:
            if not(l in curr.children):
                print("Trie doesn't start with '{0}'".format(prefix))
                return False
            curr = curr.children[l]
        print("Trie starts with '{0}'".format(prefix))
        return True


# Your Trie object will be instantiated and called as such:
trie = Trie()

trie.insert("apple")
trie.search("apple")
trie.search("appl")
trie.search("apples")
trie.search("app")
trie.startsWith("app")
trie.insert("app")
trie.search("app")