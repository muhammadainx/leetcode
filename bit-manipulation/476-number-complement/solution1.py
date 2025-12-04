"""
Approach:
Build a mask with all bits set to 1 for the length of num in binary, then XOR num with the mask to get its complement.

Time: O(n)  # where n is number of bits in num
Space: O(1)
"""

class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return 1
        
        x = num
        mask = 0

        while x:
            mask = (mask << 1) | 1
            x = x >> 1
        
        return num ^ mask
        
      


# test the function
if __name__ == "__main__":
    s = Solution()
    output = s.findComplement(5)
    print(output) # 2