"""
Approach:
Check if the two strings have the same characters by sorting both and comparing. If their sorted forms are identical, they are anagrams.

Time: O(n log n + m log m)
Space: O(n)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)



# test the function
if __name__ == "__main__":
    s = Solution()
    string1 = "racecar"
    string2 = "carrace"
    result = s.isAnagram(string1, string2)
    print(result)