# Combination Sum

 def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    pass

def recurse(candidate: List[int], target: int, solutions):
    if sum(candidates) > target:
        return
    if sum(candidates) == target:
        solutions.append(candidates)
        return
    # if sum(candidates) < target
    

test_cases = [  ([2, 3, 6, 7], 7),
                ([2, 3, 5], 8)
            ]
for case in test_cases:
    candidates, target = case
    print(combinationSum(candidates, target))