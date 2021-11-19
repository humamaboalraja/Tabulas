from data.PriorityQueue import PriorityQueue


class Graph():
    def __init__(self, graph):
        self.graph = graph
    
    def heuristic(self, current, to_find): 
        (x1, y1) = self.graph[current]["coords"] # O(1)
        (x2, y2) = self.graph[to_find]["coords"] # O(1)
        dist =  abs(x1 - x2)**2 + abs(y1 - y2)**2 # O(5)
        return dist # O(1) | T(n,m) = 1 + 1 + 5 + 1 = 4 => T(n,m) = Ω(1)
    
    def astar(self, start, to_find):
        toVisit = PriorityQueue()
        toVisit.put(start, 0)
        visitedFromVertex = {} 
        costToVertex= {}

        visitedFromVertex[start] = None 
        costToVertex[start] = 0 

        while not toVisit.empty():
            current = toVisit.get() # O(log(v))
            if current == to_find:
                path = []
                while current != start:
                    path.append(current)
                    current = visitedFromVertex[current]
                path.append(start)
                path.reverse()
                return path, "The cost is " + str(costToVertex[to_find])
            
            for neighbor, weight in self.graph[current]["neighbors"]:
                new_cost = costToVertex[current] + weight
                if neighbor not in costToVertex or new_cost < costToVertex[neighbor]:
                    costToVertex[neighbor] = new_cost
                    priority = new_cost + self.heuristic(neighbor, to_find)
                    toVisit.put(neighbor, priority)
                    visitedFromVertex[neighbor] = current

        return "No path"


graph = {
    "JFK" : {"coords": (40.730, -73.935), "neighbors": [("LAX", 92), ("LHR", 427), ("GRU", 419)]},
    "BER" : {"coords": (52.520, 13.404), "neighbors": [("FCO", 33), ("LHR", 54), ("SVO", 122)]},
    "FCO" : {"coords": (41.773, 12.239), "neighbors": [("BER", 33), ("LHR", 95), ("JNB", 351), ("DEL", 358)]},
    "LHR" : {"coords": (51.509, 0.118), "neighbors": [("JFK", 427),("BER", 54), ("FCO", 95), ("GRU", 521)]},
    "LAX" : {"coords": (34.052, -118.24), "neighbors": [("JFK", 92), ("HNL", 129), ("ICN", 567), ("SYD", 890)]},
    "GRU" : {"coords" : (-23.588, -46.658), "neighbors" : [("JFK", 419), ("LHR", 521), ("JNB", 545)]},
    "JNB" : {"coords" : (-26.134, 28.240), "neighbors" : [("FCO", 351), ("GRU", 545), ("DEL", 454)]},
    "SVO" : {"coords" : (55.751, 37.618), "neighbors" : [("BER", 122), ("PEK", 621)]},
    "DEL" : {"coords" : (28.644, 77.216), "neighbors" : [("FCO", 358), ("PEK", 779), ("JNB", 454)]},
    "SYD" : {"coords" : (-33.947, 151.179), "neighbors" : [("LAX", 890), ("ICN", 554), ("PEK", 445), ("HNL", 467)]},
    "PEK" : {"coords" : (40.072, 116.597), "neighbors" : [("SVO", 621), ("SYD", 445), ("ICN", 454), ("DEL", 779)]},
    "HNL" : {"coords" : (21.315, -157.858), "neighbors" : [("LAX", 129), ("SYD", 467)]},
    "ICN" : {"coords" : (37.532, 127.024), "neighbors" : [("LAX", 567), ("SYD", 554), ("PEK", 454)]},
}
graph = Graph(graph)
startingPoint = "GRU"
endingPoint = "PEK"
print(graph.astar(startingPoint, endingPoint))
