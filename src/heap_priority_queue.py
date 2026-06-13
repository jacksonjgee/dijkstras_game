class HeapPriorityQueue:
    def __init__(self, array=None):
        self.array = []

        if array is not None:
            for priority, item in array:
                self.add(priority, item)

    def __len__(self):
        return len(self.array)

    def is_empty(self):
        return len(self.array) == 0

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return (2 * index) + 1

    def right_child(self, index):
        return (2 * index) + 2

    def swap(self, index1, index2):
        self.array[index1], self.array[index2] = (
            self.array[index2],
            self.array[index1],
        )

    def add(self, priority, item):
        entry = (priority, item)

        self.array.append(entry)
        self.upheap_bubbling(len(self.array) - 1)

    def upheap_bubbling(self, index):
        while index > 0:
            parent_index = self.parent(index)

            if self.array[index][0] >= self.array[parent_index][0]:
                break

            self.swap(index, parent_index)
            index = parent_index

    def remove_min(self):
        if self.is_empty():
            raise IndexError("Priority queue is empty")

        self.swap(0, len(self.array) - 1)

        minimum = self.array.pop()

        if not self.is_empty():
            self.downheap_bubbling(0)

        return minimum

    def min(self):
        if self.is_empty():
            raise IndexError("Priority queue is empty")

        return self.array[0]

    def downheap_bubbling(self, index):
        while self.left_child(index) < len(self.array):
            left = self.left_child(index)
            smallest_child = left

            right = self.right_child(index)

            if (
                right < len(self.array)
                and self.array[right][0] < self.array[left][0]
            ):
                smallest_child = right

            if self.array[index][0] <= self.array[smallest_child][0]:
                break

            self.swap(index, smallest_child)
            index = smallest_child