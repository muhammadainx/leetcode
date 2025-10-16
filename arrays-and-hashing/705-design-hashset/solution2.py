"""
Approach:
Use a fixed-size boolean array of length 10^6 + 1, where each index directly represents a key.
Mark True when a key is added and False when removed. Lookup is done in O(1) using direct indexing.

Time: O(1) for each function call
Space: O(1000000) since the key is in the range [0, 1000000]
"""

class MyHashSet:

    def __init__(self):
        self.myset = [False] * 1000001
        

    def add(self, key: int) -> None:
        self.myset[key] = True
        

    def remove(self, key: int) -> None:
        self.myset[key] = False
        

    def contains(self, key: int) -> bool:
        return self.myset[key] == True



# test the function
if __name__ == "__main__":
    myHashSet= MyHashSet()
    myHashSet.add(1)      # set = [1]
    myHashSet.add(2)      # set = [1, 2]
    myHashSet.contains(1) # return True
    myHashSet.contains(3) # return False
    myHashSet.add(2)      # set [1, 2]
    myHashSet.contains(2) # return True
    myHashSet.remove(2)   # set = [1]
    myHashSet.contains(2) # return False
