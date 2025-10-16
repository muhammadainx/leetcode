"""
Approach:
Use a simple Python list to store elements.
- On add, append only if the key isn’t already present.
- On remove, delete it if it exists.
- On contains, check membership with in.

Time: O(n) for each function call (due to linear search)
Space: O(n) — for storing up to n elements.
"""

class MyHashSet:

    def __init__(self):
        self.data = []
        

    def add(self, key: int) -> None:
        if key not in self.data:
            self.data.append(key)
        

    def remove(self, key: int) -> None:
        if key in self.data:
            self.data.remove(key)
        

    def contains(self, key: int) -> bool:
        return key in self.data



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
