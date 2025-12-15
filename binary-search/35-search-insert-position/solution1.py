"""
Approach:
Use binary search on the sorted array.
If the target is found, return its index.
Otherwise, return the position where the target would be inserted to maintain sorted order.

Time: O(logn)
Space: O(1)
"""

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return left
        

# test the function
if __name__ == "__main__":
    s = Solution()
    nums = [1, 3 , 5, 6]
    target = 2
    output = s.searchInsert(nums, target)
    print(output)