# Count and Say
# Keep creating each successive string by counting lengths of 
# equal characters.
# Time: O(n * s) | Space: O(n * s)

def countAndSay(n: int) -> str:
    # Start with 1
    s = '1'

    # Calculate n - 1 layers of s (because 1st layer is '1')
    for _ in range(n - 1):
        new_s = ''
        count, prev = 0, ''
        
        # Condense string
        for c in s:
            # If character changes, add previous chunk to solution
            if not(c == prev):
                new_s += str(count) + prev if count > 0 else ''
                prev = c
                count = 0
            count += 1

        # Add last chunk
        new_s += str(count) + prev
        
        # Save new string
        s = new_s
    return s

# Driver Code
countAndSay(10)
