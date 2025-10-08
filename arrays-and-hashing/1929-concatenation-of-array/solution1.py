"""
Approach:
Loop twice through the array and append elements to build the concatenated list.

Time: O(n)
Space: O(n)
"""
from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            for num in nums:
                ans.append(num)
        return ans



# test the function
if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3]
    result = s.getConcatenation(nums)
    print(result)