"""
Approach:
1. Sort the array first.
2. After sorting, any duplicate elements will appear next to each other.
3. Traverse the array once, comparing each element with its previous one.
4. If any two consecutive elements are equal, return True.
5. If the loop completes without finding duplicates, return False.

Time: O(n log n)
Space: O(1)
"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
            
        return False



# test the function
if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3, 1]
    result = s.containsDuplicate(nums)
    print(result)