"""
Approach:
Start from 1 and repeatedly double the value until it meets or exceeds n, then return whether it equals n.

Time: O(log n)
Space: O(1)
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
      x = 1
      while x < n:
        x = x * 2
      return x == n



# test the function
if __name__ == "__main__":
    s = Solution()
    output = s.isPowerOfTwo(36)
    print(output) # False