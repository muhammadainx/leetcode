"""
Approach:
We use a hash map (defaultdict(list)) to group words that are anagrams. For each word, we sort its characters alphabetically to create a key that will be identical for all its anagrams. We then append the original word to the list corresponding to that key. Finally, we return all the grouped lists.

Time: O(n × k log k) — where n is the number of strings and k is the average length of each string (sorting each word takes O(k log k)).
Space: O(n × k) — to store all strings and their sorted keys in the hash map.
"""

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)

        for s in strs:
            sorted_s = ''.join(sorted(s))
            anagrams_dict[sorted_s].append(s)

        return list(anagrams_dict.values())



# test the function
if __name__ == "__main__":
    s = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    result = s.groupAnagrams(strs)
    print(result)