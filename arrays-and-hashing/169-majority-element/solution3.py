"""
Approach:
Use a hash map to count the frequency of each number. Track the element with the highest count as the majority element.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        candidate = 0
        maxCount = 0

        for num in nums:
            count[num] = 1 + count.get(num, 0)

            if maxCount < count[num]:
                candidate = num
                maxCount = count[num]
        
        return candidate


# test the function
if __name__ == "__main__":
    s = Solution()
    nums = [2, 2, 1, 1, 1, 2, 2]
    result = s.majorityElement(nums)
    print(result)