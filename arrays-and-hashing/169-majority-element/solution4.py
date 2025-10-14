"""
Approach:
Use Boyer–Moore Voting Algorithm — track a candidate and a count. Increment count when the current number matches the candidate; otherwise, decrement. Reset candidate when count reaches zero.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate
        


# test the function
if __name__ == "__main__":
    s = Solution()
    nums = [2, 2, 1, 1, 1, 2, 2]
    result = s.majorityElement(nums)
    print(result)