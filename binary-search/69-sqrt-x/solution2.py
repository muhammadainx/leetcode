"""
Approach:
Use binary search on the range [0, x].
Compare mid ** 2 with x to narrow the search.
Return the largest integer whose square is less than or equal to x.

Time: O(logx)
Space: O(1)
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        res = 0

        while left <= right:
            mid = left + (right - left) // 2

            if mid ** 2 < x:
                left = mid + 1
                res = mid
            elif mid ** 2 > x:
                right = mid - 1
            else:
                return mid
        
        return res

# test the function
if __name__ == "__main__":
    s = Solution()
    x = 17
    output = s.mySqrt(x)
    print(output)