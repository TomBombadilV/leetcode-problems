# Uncrossed Lines
# Use DP akin to longest common substring
# Time: O(n^2) | Space: O(n^2)

from test import test
from typing import List

def maxUncrossedLines(A: List[int], B: List[int]) -> int:
    m, n = len(A), len(B)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]  # A x B

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]

# Driver Code
cases = [   ([1, 4, 2], [1, 2, 4], 2),
            ([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2], 3),
            ([1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1], 2)
]
test(maxUncrossedLines, cases)
