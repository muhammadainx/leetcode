"""
Approach:
Use the bit trick that powers of two have exactly one set bit; n & (n - 1) clears the lowest set bit, so the result is zero only for powers of two.

Time: O(1)
Space: O(1)
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
      return n > 0 and n & (n - 1) == 0



# test the function
if __name__ == "__main__":
    s = Solution()
    output = s.isPowerOfTwo(65)
    print(output) # False