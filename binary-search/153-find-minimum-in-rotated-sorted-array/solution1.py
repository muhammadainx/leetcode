"""
Approach:
In a rotated sorted array, one half is always sorted.
Compare nums[mid] with nums[right]:

If nums[mid] > nums[right], the minimum lies to the right.
Otherwise, the minimum is at mid or to the left.

Narrow the search until both pointers converge on the minimum element.

Time: O(logn)
Space: O(1)
"""

class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]



# test the function
if __name__ == "__main__":
    s = Solution()
    nums = [4, 5, 6, 7, -11, 0, 1, 2]
    output = s.findMin(nums)
    print(output)