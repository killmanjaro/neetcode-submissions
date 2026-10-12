class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * capacity
        
    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i] = n


    def pushback(self, n: int) -> None:
        if self.getSize() == self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size += 1


    def popback(self) -> int:
        self.size -= 1
        return self.arr[self.size]


    def resize(self) -> None:
        self.new_capacity = 2 * self.capacity
        # allocate a new array
        self.new_arr = [0] * self.new_capacity
        # copy every existing element from old array into new
        for i in range(self.capacity):
            self.new_arr[i] = self.arr[i]

        # replace old array with the new one
        self.arr = self.new_arr
        self.capacity = self.new_capacity



    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
