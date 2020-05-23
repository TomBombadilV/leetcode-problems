# Interval List Intersections

from typing import List

def intervalIntersection(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    res = []
    while A and B:
        a, b = A[0], B[0]
        if b[1] < a[0]:
            B = B[1:]
        elif b[0] > a[1]:
            A = A[1:]
        else:  # Overlap
            res.append([max(a[0], b[0]), min(a[1], b[1])])
            if b[1] > a[1]:
                A = A[1:]
            else:
                B = B[1:]
    return res

# Driver Code
A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]
intervalIntersection(A, B)
