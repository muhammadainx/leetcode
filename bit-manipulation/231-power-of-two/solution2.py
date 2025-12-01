"""
Approach:
Recursively divide n by 2 while it’s even; if it reaches 1, it’s a power of two.

Time: O(log n)
Space: O(log n)   # recursion depth
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
      if n == 1:
         return True
      if n <= 0 or n % 2 == 1:
         return False
      return self.isPowerOfTwo(n // 2)



# test the function
if __name__ == "__main__":
    s = Solution()
    output = s.isPowerOfTwo(256)
    print(output) # True