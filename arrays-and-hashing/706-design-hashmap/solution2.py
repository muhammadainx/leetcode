"""
Approach:
Use a fixed bucket array with separate chaining via linked lists. Operations run in average O(n/k) time due to traversal within a bucket, with space cost for buckets plus stored nodes.

Time: O(n/k) for each function call
Space: O(k + m)
"""
class ListNode:

    def __init__(self, key = -1, value = -1, next = None):
        self.key = key
        self.value = value
        self.next = next

class MyHashMap:

    def __init__(self):
        self.map = [ListNode() for _ in range(1000)]


    def hash(self, key):
        return key % len(self.map)
        

    def put(self, key: int, value: int) -> None:
        cur = self.map[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next.value = value
                return
            cur = cur.next
        
        cur.next = ListNode(key, value)


    def get(self, key: int) -> int:
        cur = self.map[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                return cur.next.value
            cur = cur.next
        
        return -1


    def remove(self, key: int) -> None:
        cur = self.map[self.hash(key)]
        while cur.next:
             if cur.next.key == key:
                cur.next = cur.next.next
                return
             cur = cur.next



# test the function
if __name__ == "__main__":
    obj = MyHashMap()
    obj.put(1, 10)
    print(obj.get(1))   # output: 10
    obj.remove(1)
    print(obj.get(1))   # output: -1
    
