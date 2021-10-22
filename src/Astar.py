from data.PriorityQueue import PriorityQueue
from haversine import haversine, Unit

class astarGraph():
    def __init__(self, graph):
        self.graph = graph
    
    def heuristic(self, current, to_find):
        # The heuristic method estimates the distance between a neighbor and the vertex to find
        return haversine((current['y'], current['x']),(to_find['y'], to_find['x']),unit=Unit.METERS)
    
    def astar(self, start, to_find):
        toVisit = PriorityQueue()
        toVisit.put(start, 0)
        visitedFromVertex = {}
        costToVertex= {}
        visitedFromVertex[start] = None 
        costToVertex[start] = 0
        exploredVertices = 0
        exploredEdges = 0

        while not toVisit.empty():
            current = toVisit.get()
            exploredVertices += 1
            if current == to_find:
                path = []
                while current != start:
                    path.append(current)
                    current = visitedFromVertex[current]
                path.append(start)
                path.reverse()
                return path, exploredVertices, exploredEdges, costToVertex[to_find]