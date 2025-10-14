"""
Approach:
Sort the array; the middle element will always be the majority element since it appears more than ⌊n/2⌋ times.

Time: O(n log n)
Space: O(1) (ignoring sorting overhead)
"""

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]



# test the function
if __name__ == "__main__":
    s = Solution()
    nums = [2, 2, 1, 1, 1, 2, 2]
    result = s.majorityElement(nums)
    print(result)