"""
Approach:
Sort the strings lexicographically; the common prefix of the first and last strings after sorting is the common prefix of the entire list. Compare characters of these two strings until they differ.

Time: O(n log n + m), where n = number of strings, m = length of the shortest string
Space: O(1)

"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()

        smallest = strs[0]
        largest = strs[len(strs) - 1]
        
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