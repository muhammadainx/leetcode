"""
Approach:
Approach:
Use a direct-address table of fixed size 1,000,001. Store values directly at index key. All operations, put, get, remove run in constant time with fixed memory overhead.

Time: O(1) for each function call.
Space: O(1000000) since the key is in the range [0,1000000]
"""

class MyHashMap:

    def __init__(self):
        self.map = [-1] * 1000001
        
    def put(self, key: int, value: int) -> None:
        self.map[key] = value
        
    def get(self, key: int) -> int:
        return self.map[key]

    def remove(self, key: int) -> None:
        self.map[key] = -1

# test the function
if __name__ == "__main__":
    obj = MyHashMap()
    obj.put(1, 10)
    print(obj.get(1))   # output: 10
    obj.remove(1)
    print(obj.get(1))   # output: -1

