"""
Approach:
Use binary search on the sorted array.
Maintain two pointers (left and right) and repeatedly check the middle element.
If the middle value is smaller than the target, discard the left half; if larger, discard the right half.
Continue until the target is found or the search space is empty.

Time: O(logn)
Space: O(1)
"""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
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
        
        return -1
 

# test the function
if __name__ == "__main__":
    s = Solution()
    nums = [-1,0,3,5,9,12]
    target = 9
    output = s.search(nums, target)
    print(output)