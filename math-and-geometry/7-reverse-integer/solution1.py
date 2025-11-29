"""
Approach:
Reverse the integer by extracting its digits one by one from the least significant digit. Track the sign separately and apply it at the end. Before adding each digit, check for overflow against 32-bit signed integer limits.

Time: O(k) where k is the number of digits in x
Space: O(1)
"""

class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2**31 - 1

        res = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x:
            digit = x % 10
            x = x // 10

            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0
            
            res = res * 10 + digit
        
        return sign * res   
      


# test the function
if __name__ == "__main__":
    s = Solution()
    x = 123
    output = s.reverse(x)
    print(output) # 321