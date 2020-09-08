"""
You are given two strings s and t of the same length. You want to change s to t. 
Changing the i-th character of s to i-th character of t costs |s[i] - t[i]| that is, 
the absolute difference between the ASCII values of the characters.

You are also given an integer maxCost.

Return the maximum length of a substring of s that can be changed to be the same as 
the corresponding substring of twith a cost less than or equal to maxCost.

If there is no substring from s that can be changed to its corresponding substring 
from t, return 0.
"""

class EqualSubstrings:
    def equal_sub_string(self, s: str, t: str, maxCost: int):
        prefix_cost = self.calculate_prefix(s, t)
        print(prefix_cost)
        l, r, max_len = 0, 0, 0
        while (r < len(s)):
            if (prefix_cost[r]-prefix_cost[l]<=maxCost):
                max_len = max(max_len, r-l)
                r += 1
            else:
                l += 1
        return max_len

    def calculate_prefix(self, s: str, t: str):
        prefix, cur = [], 0
        prefix.append(0)
        for i in range(len(s)):
            cur = abs(ord(s[i])-ord(t[i]))
            prefix.append(prefix[-1]+cur)
        return prefix

test = EqualSubstrings()
print(test.equal_sub_string("abcd", "cdef", 3))



 