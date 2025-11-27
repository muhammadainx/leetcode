"""
Approach:
Use the digital root property. The repeated digit sum of a number
is equal to num % 9, except multiples of 9 which return 9 (except 0).

Time: O(1)
Space: O(1)
"""

class Solution:
   def addDigits(self, num: int) -> int:
       if num == 0:
           return 0
       
       if num % 9 == 0:
           return 9
       
       return num % 9



# test the function
if __name__ == "__main__":
    s = Solution()
    num = 38
    output = s.addDigits(num)
    print(output) # 2