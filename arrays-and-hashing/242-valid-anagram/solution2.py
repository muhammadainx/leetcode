"""
Approach:
Count the frequency of each character in both strings using hash maps (dictionaries).
If the frequency maps are identical, the strings are anagrams; otherwise, they’re not.

Time: O(n) — iterate through both strings once.
Space: O(1) — limited to 26 letters (or O(n) for general character sets).
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        return countS == countT




# test the function
if __name__ == "__main__":
    s = Solution()
    string1 = "racecar"
    string2 = "carrace"
    result = s.isAnagram(string1, string2)
    print(result)