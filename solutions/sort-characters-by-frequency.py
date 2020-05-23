# Sort Characters by Frequency

from collections import Counter

def frequencySort(s: str) -> str:
    res = ''
    freq = Counter(s).most_common()
    for c in freq:
        res += c[0] * c[1]
        freq = freq[1:]
    return res

# Driver Code
print(frequencySort('tree'))
