"""
Approach:
- We use a brute-force nested loop approach to check for duplicates.
- For each element `nums[i]`, we compare it with every subsequent element `nums[j]` (where j > i).
- If any two elements are equal, we immediately return True (duplicate found).
- If no such pair is found after checking all elements, we return False.

Time: O(n^2)
Space: O(1)

Note:
This approach is simple but inefficient for large input sizes. 
It will cause a **TLE (Time Limit Exceeded)** error on large datasets because 
of the quadratic time complexity (n² comparisons).
"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        
        return False




# test the function
if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3, 1]
    result = s.containsDuplicate(nums)
    print(result)