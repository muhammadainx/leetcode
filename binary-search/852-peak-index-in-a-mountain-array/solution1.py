"""
Approach:
A mountain array increases then decreases.
Use binary search to compare arr[mid] with arr[mid + 1]:

If increasing, the peak is to the right.
If decreasing, the peak is at mid or to the left.

Shrink the search space until both pointers meet at the peak index.

Time: O(logn)
Space: O(1)
"""

class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        left, right = 0, len(arr) - 1

        while left < right:
            mid = left + (right - left) // 2

            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left




# test the function
if __name__ == "__main__":
    s = Solution()
    nums = [0, 10, 5, 2]
    output = s.peakIndexInMountainArray(nums)
    print(output)