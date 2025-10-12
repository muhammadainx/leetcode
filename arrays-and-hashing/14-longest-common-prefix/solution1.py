"""
Approach (Horizontal Scanning):
Start with the first string as the initial prefix. For each subsequent string, compare characters until they differ, trimming the prefix to the common part. Stop early if the prefix becomes empty.

Time: O(n * m)
Space: O(1)
"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for i in range(1, len(strs)):
            j = 0
            while j < min(len(prefix), len(strs[i])):
                if prefix[j] != strs[i][j]:
                    break
                j += 1
            prefix = prefix[:j]
        
        return prefix
            
        


# test the function
if __name__ == "__main__":
    s = Solution()
    strs = ["flower","flow","flight"]
    result = s.longestCommonPrefix(strs)
    print(result)