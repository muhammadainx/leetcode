"""
Approach:
Create a new array twice the length of the input. 
Copy each element from the original array into both halves of the new array.

Time: O(n)
Space: O(n)
"""

from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n)

        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]

        return ans



# test the function
if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3]
    result = s.getConcatenation(nums)
    print(result)