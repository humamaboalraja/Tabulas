import osmnx as ox
from data.PriorityQueue import PriorityQueue

from haversine import haversine, Unit

class astarGraph():
    def __init__(self, graph):
        self.graph = graph
    
    def heuristic(self, current, to_find):
        # The heuristic method estimates the distance between a neighbor and the vertex to find
        return haversine((current['y'], current['x']),(to_find['y'], to_find['x']),unit=Unit.METERS)