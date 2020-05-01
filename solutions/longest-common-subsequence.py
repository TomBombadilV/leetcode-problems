# Longest Common Subsequence
# Use a matrix to memoize checking every prefix against every other prefix.
# Time: O(m * n) | Space: O(m * n)

def longestCommonSubsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    # Pad matrix wtih 0s on left and top
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            # If new chars are equal, add 1 to lcs of prefixes excluding new chars
            if text1[i] == text2[j]:
                dp[i + 1][j + 1] = 1 + dp[i][j]
            # If new chars not equal, max lcs so far is lcs of prefix excluding char1
            # or lcs of prefix excluding char2
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
    return dp[-1][-1]

# Driver Code
cases = [ ('abcde', 'ace', 3),
          ('abc', 'abc', 3),
          ('abc', 'def', 0),
          ('carolyn', 'roy', 3),
          ('bsbininm', 'jmjkbkjkv', 1),
          ('oxcpqrsvwf', 'shmtulqrypy', 2)
]
for case in cases:
    a, b, expected = case
    res = longestCommonSubsequence_b(a, b)
    print("Passed" if res == expected else "Failed {0} with {1} expected {2}".\
          format((a, b), res, expected))
