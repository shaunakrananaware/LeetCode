class MyHashSet:

    def __init__(self):
        self.arr = []

    def add(self, key: int) -> None:
        if key not in self.arr:
            self.arr.append(key)

    def remove(self, key: int) -> None:
        new_arr = []
        for idx in range(len(self.arr)):
            if self.arr[idx] == key:
                continue
            new_arr.append(self.arr[idx])
        
        self.arr = new_arr

    def contains(self, key: int) -> bool:
        for idx in range(len(self.arr)):
            if self.arr[idx] == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)