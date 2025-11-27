"""
Approach:
Repeatedly sum the digits of the number until it becomes a single digit.
Extract each digit using modulo and integer division, accumulate the sum,
and replace the number with the computed sum.

Time: O(k)  where k is the number of digits processed (very small, bounded)
Space: O(1)
"""

class Solution:
   def addDigits(self, num: int) -> int:
      while num >= 10:
        digit_sum = 0
        while num > 0:
          digit_sum += num % 10
          num //= 10
        num = digit_sum
      
      return num
      


# test the function
if __name__ == "__main__":
    s = Solution()
    num = 38
    output = s.addDigits(num)
    print(output) # 2