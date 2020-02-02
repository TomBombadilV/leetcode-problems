# Nth Tribonacci Number
# Alternate iterative solution

def tribonacci(n: int) -> int:
    i, j, k = 0, 0, 1
    for _ in range(n - 2):
        i, j, k = j, k, i + j + k
    return 0 if n == 0 else i + j + k

print(tribonacci(0))