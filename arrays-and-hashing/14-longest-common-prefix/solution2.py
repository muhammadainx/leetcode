"""
Approach (Vertical Scanning):
We compare characters column by column across all strings.
Starting from the first character, we check if every string has the same character at that position.
If a mismatch is found or any string ends, we return the prefix formed up to that point.
If no mismatch occurs, the entire first string is the common prefix.

Time: O(n * m), where n is the number of strings and m is the length of the shortest string.
Space: O(1)
"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return strs[0][:i]
        
        return strs[0]



# test the function
if __name__ == "__main__":
    s = Solution()
    strs = ["flower","flow","flight"]
    result = s.longestCommonPrefix(strs)
    print(result)