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
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def find_left():
            left = 0
            right = len(nums) - 1
            result = -1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    result = mid
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return result
        
        def find_right():
            left = 0
            right = len(nums) - 1
            result = -1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    result = mid
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return result

        if not nums:
            return [-1, -1]
        
        left_Position = find_left()
        if left_Position == -1:
            return [-1, -1]

        right_Position = find_right()

        return [left_Position, right_Position]

        
 

# test the function
if __name__ == "__main__":
    s = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    output = s.searchRange(nums, target)
    print(output)