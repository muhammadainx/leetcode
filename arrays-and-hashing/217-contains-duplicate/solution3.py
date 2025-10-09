"""
Approach:
Use a set to keep track of seen numbers.  
Iterate through the list, and if a number already exists in the set, return True (duplicate found).  
Otherwise, add it to the set. If no duplicates are found after the loop, return False.

Time: O(n)
Space: O(n)
"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False



# test the function
if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3, 1]
    result = s.containsDuplicate(nums)
    print(result)