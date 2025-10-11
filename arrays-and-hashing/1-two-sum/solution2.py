"""
Approach:
Store each element with its original index, then sort the array by values.
Use the two-pointer technique to find two numbers whose sum equals the target.
Return their original indices in increasing order.

Time: O(n log n)
Space: O(n)


"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []

        for i in range(len(nums)):
            A.append([nums[i], i])

        A.sort()

        i = 0
        j = len(nums) - 1

        while i < j:
            curr = A[i][0] + A[j][0]

            if curr == target:
                return [min(A[i][1], A[j][1]), max(A[i][1], A[j][1])]
            elif curr < target:
                i += 1
            else:
                j -= 1
       



# test the function
if __name__ == "__main__":
    s = Solution()
    nums = [4, 5, 6]
    target = 10
    result = s.twoSum(nums, target)
    print(result)