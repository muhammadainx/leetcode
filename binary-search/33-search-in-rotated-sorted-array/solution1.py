"""
Approach:
In a rotated sorted array, one half is always sorted.

At each step:
Check if nums[mid] is the target.
Determine which half is sorted.

Decide whether the target lies in the sorted half; if yes, search there, otherwise search the other half.

Continue until the target is found or the range is exhausted.

Time: O(logn)
Space: O(1)
"""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[left]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1




# test the function
if __name__ == "__main__":
    s = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    output = s.search(nums, target)
    print(output)