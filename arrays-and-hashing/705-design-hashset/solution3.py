"""
Approach:
Implement a hash set using separate chaining with a fixed number of buckets (1000). Each bucket stores keys in a list. The hash function maps a key to its bucket using key % 1000.

Time:
- Average: O(1) for each function call
- Worst-case (all keys in one bucket): O(n)

Space: O(n) — for storing up to n keys across buckets.
"""

class MyHashSet:

    def __init__(self):
        self.bucket_size = 1000
        self.buckets = []
        for _ in range(self.bucket_size):
            self.buckets.append([])

    def _hash(self, key):
        return key % 1000

    def add(self, key: int) -> None:
        bucket = self.buckets[self._hash(key)]
        if key not in bucket:
            bucket.append(key)

        

    def remove(self, key: int) -> None:
        bucket = self.buckets[self._hash(key)]
        if key in bucket:
            bucket.remove(key)
        

    def contains(self, key: int) -> bool:
        bucket = self.buckets[self._hash(key)]
        return key in bucket
        


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
