# Word Search
from collections import defaultdict
from typing import List

"""def exist(board: List[List[str]], word: str) -> bool:
    # Fill dictionary of adjacent chars
    adjacent = defaultdict(list)
    n, m = len(board), len(board[0])
    for i in range(n):
        for j in range(m):
            if i > 0:
                adjacent[(board[i][j], (i, j))].append((board[i-1][j], (i-1, j)))
            if i < n - 1:
                adjacent[(board[i][j], (i, j))].append((board[i+1][j], (i+1, j)))
            if j > 0:
                adjacent[(board[i][j], (i, j))].append((board[i][j-1], (i, j-1)))
            if j < m - 1:
                adjacent[(board[i][j], (i, j))].append((board[i-1][j+1], (i-1, j+1)))
    # Check if word exists
    char, next_char  = word[0], word[1]
    potential = [k for k in adjacent if k[0] == curr]
    for p in potential:
        
    print(curr, keys)"""
def exist(board: List[List[str]], word: str) -> bool:
    return backtrack(board, word)

def backtrack(adjacents, board: List[List[str]], word: str) -> bool:
    if len(word) == 0:
        return True
    
                    

board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
words = ["ABCCED", "SEE", "ABCB"]
for word in words:
    print("{0} {1}".format(word, "exists" if exist(board, word) else "doesn't exist"))