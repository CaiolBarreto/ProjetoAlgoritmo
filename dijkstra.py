class Heap:
    def __init__(self, heap_list):
        self.heap = heap_list

    @staticmethod
    def getParent(index):
        return (index - 1) // 2

    def getLeftChild(self, index):
        left_index = 2 * index + 1
        if left_index < len(self.heap) - 1:
            return left_index

    def getRightChild(self, index):
        right_index = 2 * index + 2
        if right_index < len(self.heap) - 1:
            return right_index

    def hasParent(self, index):
        return self.getParent(index) > 0

    def hasChildren(self, index):
        left = self.getLeftChild(index)
        right = self.getRightChild(index)
        if left is None and right is None:
            return False
        else:
            return True

    def smallestChild(self, left_child_index, right_child_index):
        if left_child_index is None:
            return right_child_index
        elif right_child_index is None:
            return left_child_index
        elif self.heap[left_child_index][0] <= self.heap[right_child_index][0]:
            return left_child_index
        else:
            return right_child_index

    def bubble_up(self, index):
        while self.hasParent(index):
            if self.heap[index][0] < self.heap[self.getParent(index)][0]:
                self.heap[index], self.heap[self.getParent(index)] = self.heap[self.getParent(index)], self.heap[index]
            index = self.getParent(index)

    def bubble_down(self, index):
        left_child_index, right_child_index = self.getLeftChild(index), self.getRightChild(index)
        while left_child_index is not None and right_child_index is not None:
            smallest_index = self.smallestChild(left_child_index, right_child_index)
            self.heap[index], self.heap[smallest_index] = self.heap[smallest_index], self.heap[index]
            left_child_index, right_child_index = self.getLeftChild(smallest_index), self.getRightChild(smallest_index)

    def push(self, value):
        self.heap.append(value)
        self.bubble_up(len(self.heap) - 1)

    def heap_pop(self, index):
        self.heap[index], self.heap[-1] = self.heap[-1], self.heap[index]
        elim = self.heap.pop(len(self.heap) - 1)
        if self.hasChildren(index):
            self.bubble_down(index)
        return elim


def dijkstra(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0
    heapq = Heap([(0, starting_vertex)])
    priority_queue = heapq.heap
    while len(priority_queue) > 0:
        current_distance, current_vertex = heapq.heap_pop(0)
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.push((distance, neighbor))
    return distances


example_graph = {
    'U': {'V': 2, 'W': 5, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}

