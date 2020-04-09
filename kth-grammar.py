# Convert string '0' to the nth iteration by changing each '0' into '01' and 
# each '1' into '10'. Return the kth character in the nth string.

def kthGrammar(self, N: int, K: int) -> int:
    # Convert to 0-indexing
    N, K = N - 1, K - 1
    
    def recurse(n: int, k: int) -> int:
        if n == 0:
            return 0
        i = recurse(n - 1, k // 2)
        if i == 0:
            return 0 if k % 2 == 0 else 1
        else:
            return 1 if k % 2 == 0 else 0
    
    return recurse(N, K)
