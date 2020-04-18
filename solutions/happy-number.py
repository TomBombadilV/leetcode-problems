# Sum the squares of the digits of given num
def get_sum(n: int) -> int:
    s = 0
    while n:
        s += (n % 10) ** 2
        n = n // 10
    return s

def isHappy(n: int) -> bool:
    sum_set = set()
    curr_sum = n
    # While current sum hasn't been calculated before (we're not in a loop) 
    while not(curr_sum in sum_set):
        # Add current sum to the set
        sum_set.add(curr_sum)
        # Get new sum
        curr_sum = get_sum(curr_sum)
        if curr_sum == 1:
            return True
    # Encountered a loop
    return False

for i in range(10):
    print(i, isHappy(i))
