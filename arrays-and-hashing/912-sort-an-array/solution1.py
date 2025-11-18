"""
Approach:
Use Merge Sort, a divide-and-conquer sorting algorithm:
1. Recursively split the array into two halves until each part has one element.
2. Merge the halves back together in sorted order using a temporary left and right subarray.

Time: O(nlogn)
Space: O(n)
"""

from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(array, left, mid, right):
            left_part = array[left: mid + 1]
            right_part = array[mid + 1: right + 1]

            i, j = 0, 0
            k = left
            

            while i < len(left_part) and j < len(right_part):
                if left_part[i] <= right_part[j]:
                    array[k] = left_part[i]
                    i += 1
                else:
                    array[k] = right_part[j]
                    j += 1
                k += 1
            
            while i < len(left_part):
                array[k] = left_part[i]
                i += 1
                k += 1
            
            while j < len(right_part):
                array[k] = right_part[j]
                j += 1
                k += 1 

        
        def mergeSort(array, left, right):
            if left < right:
                mid = (left + right) // 2
                mergeSort(array, left, mid)
                mergeSort(array, mid + 1, right)
                merge(array, left, mid, right)
        
        mergeSort(nums, 0, len(nums) - 1)
        return nums
        


# test the function
if __name__ == "__main__":
    s = Solution()
    print(s.sortArray([5, 1, 1, 2, 0, 0]))     # [0, 0, 1, 1, 2, 5]
 
    