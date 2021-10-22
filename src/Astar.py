from data.PriorityQueue import PriorityQueue
from haversine import haversine, Unit

class astarGraph():
    def __init__(self, graph):
        self.graph = graph
    
    def heuristic(self, current, to_find):
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
            
            for neighbor in list(self.graph.neighbors(current)):
                distance = self.graph[current][neighbor][0]["length"]
                newCost = costToVertex[current] + distance
                exploredEdges += 1
                if neighbor not in costToVertex or newCost < costToVertex[neighbor]:
                    costToVertex[neighbor] = newCost
                    priority = newCost + self.heuristic(self.graph.nodes[neighbor], self.graph.nodes[to_find])
                    toVisit.put(neighbor, priority)
                    visitedFromVertex[neighbor] = current
        return