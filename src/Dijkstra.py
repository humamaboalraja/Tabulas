import osmnx as ox
from data.PriorityQueue import PriorityQueue


class dijkstraGraph():
    def __init__(self, graph):
        self.graph = graph
    
    def dijkstra(self, start, to_find):
        toVisit = PriorityQueue()
        toVisit.put(start, 0)
        visitedFromVertex = {}
        costToVertex= {}
        visitedFromVertex[start] = None 
        costToVertex[start] = 0
        # keep track of the number of explored vertices and edges
        vertices_explored = 0
        edges_explored = 0

        while not toVisit.empty():
            current = toVisit.get()
            vertices_explored += 1
            if current == to_find:
                path = []
                while current != start:
                    path.append(current)
                    current = visitedFromVertex[current]
                path.append(start)
                path.reverse()
                return path, vertices_explored, edges_explored, costToVertex[to_find]
            
            for neighbor in list(self.graph.neighbors(current)):
                distance = self.graph[current][neighbor][0]["length"]
                newCost = costToVertex[current] + distance
                edges_explored += 1
                if neighbor not in costToVertex or newCost < costToVertex[neighbor]:
                    costToVertex[neighbor] = newCost
                    priority = newCost
                    toVisit.put(neighbor, priority)
                    visitedFromVertex[neighbor] = current
        return
