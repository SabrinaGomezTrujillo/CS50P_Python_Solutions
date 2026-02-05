class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if n < 0:
            raise ValueError("Cannot deposit a negative number of cookies")
        elif self._size + n > self._capacity:
            raise ValueError("Cannot deposit more cookies than the jar's capacity")
        else:
            self._size += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError("Cannot withdraw a negative number of cookies")
        elif self._size - n < 0:
            raise ValueError("Cannot withdraw more cookies than the jar's current size")
        else:
            self._size -= n

    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        if capacity < self._size:
            raise ValueError("Capacity cannot be less than the jar's current size")
        else:
            self._capacity = capacity

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self,size):
        if size < 0:
            raise ValueError("Size must be a non-negative integer")
        elif size > self._capacity:
            raise ValueError("Size cannot exceed the jar's capacity")
        else:
            self._size = size

