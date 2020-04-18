# Minimum Window Substring

from collections import defaultdict

def minWindow(s: str, t: str) -> str:
    dic = defaultdict(int)