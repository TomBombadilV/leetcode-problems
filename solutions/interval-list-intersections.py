# Interval List Intersections
# Iterate through both interval lists, throwing away an interval if its too small
# and preserving any overlaps.
# Time: O(A + B) | Space: O(max(A, B))

from typing import List

def intervalIntersection(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    res = []
    i = j = 0
    
    while i < len(A) and j < len(B):
        a, b = A[i], B[j]
        # If entire B interval comes before A, ignore B interval
        if b[1] < a[0]:
            j += 1
        # If entire A interval comes before B, ignore A interval
        elif b[0] > a[1]:
            i += 1
        # If overlap, save overlap (max start, min end)
        else:
            res.append([max(a[0], b[0]), min(a[1], b[1])])
            # Throw away interval that has lower end number
            if b[1] > a[1]:
                i += 1
            else:
                j += 1
    return res

# Driver Code
A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]
intervalIntersection(A, B)
