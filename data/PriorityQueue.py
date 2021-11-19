import heapq
class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return not self.elements
    
    def put(self, item, priority): # O(log n)
        heapq.heappush(self.elements, (priority, item))
        # When new element is added to the heap the order of elements gets adjusted to maintain heap structure.
    
    def get(self): # O(log n)
        return heapq.heappop(self.elements)[1]
        # This method removes and returns first element of the heap. When removing first element the order of other elements gets adjusted to maintain heap structure. If the heap was empty, then IndexError is raised.