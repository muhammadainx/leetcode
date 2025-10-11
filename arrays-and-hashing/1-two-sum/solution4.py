"""
Approach:
Iterate once while storing each number’s index in a dictionary.
For each number, check if its complement (target - num) already exists in the dictionary.
Return the pair of indices as soon as a match is found.

Time: O(n)
Space: O(n)


"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val => index

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in prevMap:
                return [prevMap[diff], i]
            
            prevMap[nums[i]] = i


# test the function
if __name__ == "__main__":
    s = Solution()
    nums = [4, 5, 6]
    target = 10
    result = s.twoSum(nums, target)
    print(result)