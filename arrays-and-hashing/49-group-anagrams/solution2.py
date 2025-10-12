"""
Approach:
Use a hash map to group words with the same character frequency. For each string, count occurrences of each letter (26-length array) and use its tuple form as the key. Words with identical counts are grouped together.

Time: O(n × k) — where n is the number of strings and k is the average length of each string.
Space: O(n × k) — for storing the grouped anagrams and their keys.
"""

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1

            key = tuple(count)
            anagrams_dict[key].append(s)

        return list(anagrams_dict.values())



# test the function
if __name__ == "__main__":
    s = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    result = s.groupAnagrams(strs)
    print(result)