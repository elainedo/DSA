'''
Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

'''

def combinationSum(candidates, target):
    result = []
    def backtrack(candidates, cur_list, target, start):
        if target < 0: return
        if target == 0:
            result.append(list(cur_list))
            return
        for i in range(start, len(candidates)):
            cur_list.append(candidates[i])
            backtrack(candidates, cur_list, target-candidates[i], i)
            cur_list.pop()
    backtrack(candidates, [], target, 0)
    return result

print(combinationSum([2, 3, 6, 7], 7))


