"""
Approach:
Check if both strings have the same frequency of each character.
Use a fixed-size array of 26 counts (for letters a–z), incrementing for s and decrementing for t.
If all counts return to zero, the strings are anagrams.

Time Complexity: O(n) — single pass through both strings.
Space Complexity: O(1) — constant space for 26 letters.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord("a")] += 1
            count[ord(t[i]) - ord("a")] -= 1

        for val in count:
            if val != 0:
                return False
            
        return True



# test the function
if __name__ == "__main__":
    s = Solution()
    string1 = "racecar"
    string2 = "carrace"
    result = s.isAnagram(string1, string2)
    print(result)