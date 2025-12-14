"""
Approach:
Apply recursive binary search on the sorted array.
At each step, compare the middle element with the target.
If it matches, return its index; otherwise, recursively search the appropriate half.
Stop when the search range becomes invalid.

Time: O(log n)
Space: O(log n) (due to recursion stack)
"""

class Solution:
    def binary_search(self, left: int, right: int, nums: list[int], target: int) -> int:
        if left > right:
            return -1
        
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        
        if nums[mid] < target:
            return self.binary_search(mid + 1, right, nums, target)
        
        return self.binary_search(left, mid - 1, nums, target)
    
    def search(self, nums: list[int], target: int) -> int:
        return self.binary_search(0, len(nums) - 1, nums, target)
         



# test the function
if __name__ == "__main__":
    s = Solution()
    nums = [-1,0,3,5,9,12]
    target = 9
    output = s.search(nums, target)
    print(output)