"""
Approach:
Use a brute-force nested loop to check every possible pair (i, j).
Return the indices of the first pair whose sum equals the target.

Time: O(n^2)
Space: O(1)


"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []



# test the function
if __name__ == "__main__":
    s = Solution()
    nums = [4, 5, 6]
    target = 10
    result = s.twoSum(nums, target)
    print(result)