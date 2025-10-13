"""
Approach:
Use two pointers — `i` to iterate and `n` as the last valid index.
When nums[i] == val, swap it with nums[n] and decrease n (to skip the removed element).
Otherwise, move i forward. Return i as the new length.

Time: O(n)   # each element is processed at most once
Space: O(1)  # in-place modification
"""

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums) - 1

        while i <= n:
            if nums[i] == val:
                nums[i], nums[n] = nums[n], nums[i]
                n -= 1
            else:
                i += 1
        return i

# test the function
if __name__ == "__main__":
    s = Solution()
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    result = s.removeElement(nums, val)
    print(result)