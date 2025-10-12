"""
Approach (Lexicographical Comparison):
The smallest and largest strings in lexicographical order will differ the most.
By comparing these two, we can find the longest common prefix shared by all strings — since any mismatch between them implies a mismatch with at least one other string.

Time Complexity: O(n · m), where n is the number of strings and m is the average string length (due to min/max comparisons).
Space Complexity: O(1).
"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest = min(strs)
        largest = max(strs)
        
        for i in range(len(smallest)):
            if smallest[i] != largest[i]:
                return smallest[:i]
        
        return smallest



# test the function
if __name__ == "__main__":
    s = Solution()
    strs = ["flower","flow","flight"]
    result = s.longestCommonPrefix(strs)
    print(result)