"""
Approach:
Store each number and its index in a dictionary.
For each element, check if its complement (target - num) exists in the dictionary
and return their indices when found.

Time: O(n)
Space: O(n)


"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {} # val -> index

        for i in range(len(nums)):
            indices[nums[i]] = i
        
        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]



# test the function
if __name__ == "__main__":
    s = Solution()
    nums = [4, 5, 6]
    target = 10
    result = s.twoSum(nums, target)
    print(result)