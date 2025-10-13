"""
Approach:

Time: O() 
Space: O()
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