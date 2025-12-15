"""
Approach:
Iterate from 1 upward and check squares.
Return the largest integer whose square is less than or equal to x.

Time: O(x)
Space: O(1)
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        res = 1
        for i in range(1, x + 1):
            if i ** 2 > x:
                return res
            res = i

        return res

# test the function
if __name__ == "__main__":
    s = Solution()
    x = 17
    output = s.mySqrt(x)
    print(output)