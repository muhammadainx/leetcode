"""
Approach:
Check if n is a divisor of 2**30, since all powers of two ≤ 2³⁰ divide it evenly.

Time: O(1)
Space: O(1)
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
      return n > 0 and ((1 << 30) % n) == 0


# test the function
if __name__ == "__main__":
    s = Solution()
    output = s.isPowerOfTwo(1024)
    print(output) # False