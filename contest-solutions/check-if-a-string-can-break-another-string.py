# Check if a String Can Break Another String
# Sort strings and compare if every character of one is greater than the other.
# Time: O(max(s1, s2)) | Space: O(s1 + s2))

def checkIfCanBreak(s1: str, s2: str) -> bool:
    s1_s, s2_s = sorted(s1), sorted(s2)
    broken_a = True
    # Check if s2 breaks s1
    for i in range(len(s1)):
        if not(s2_s[i]) >= s1_s[i]:
            broken_a = False
    # Check if s1 breaks s2
    broken_b = True
    for i in range(len(s1)):
        if not(s2_s[i]) <= s1_s[i]:
            broken_b = False
    # If either is broken, return True
    return broken_a or broken_b

# Driver Code
cases = [('abc', 'xya', True), 
         ('abe', 'acd', False), 
         ('leetcodee', 'interview', True)]
for case in cases:
    s1, s2, expected = case
    res = checkIfCanBreak(s1, s2)
    print("Passed" if res == expected else "{0} failed with {1} expected {2}".\
          format((s1, s2), res, expected))
