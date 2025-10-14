"""
Approach:
For each element, count how many times it appears in the array. Return the element whose count exceeds ⌊n/2⌋.

Time: O(n^2)
Space: O(1)
"""

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            count = 0
            for j in range(n):
                if nums[j] == nums[i]:
                    count += 1
            
            if count > (n // 2):
                return nums[i]



# test the function
if __name__ == "__main__":
    s = Solution()
    nums = [2, 2, 1, 1, 1, 2, 2]
    result = s.majorityElement(nums)
    print(result)