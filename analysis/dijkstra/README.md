# Dijkstra's Algorithm


In a weighted network, we use Dijkstra's Algorithm to discover the shortest distance between two vertices. The weight of the edges must be positive for this algorithm to succeed. It can also be tweaked to find the distance between a vertex and all the other vertices in a graph.

<br>

### **Algorithm's workflow**
---

1. Initialize three auxiliary data structures to keep track of the vertices to visit (starting from the starting vertex), from which adjacent vertex a vertex has been visited (None for the starting vertex); and the cost to get from the starting vertex to that one (0 for the starting vertex). We will call these data structures `a`, `b`, and `c` respectively for simplicity;
2. Set the current vertex to be the one with the lowest "cost" in `a` and remove it from `a` (in the first iteration, it will be the starting vertex);
3. If the current vertex is the vertex to find, reconstruct and return the path to that vertex;
4. Otherwise, for each of its neighbors `n`, calculate the "cost" to get there and if they are not in `c`, or if they are but this new "cost" is lower than the previous one: update its value in `c`, add it to `a` with its new "cost" as priority, and set it as visited from the current node in `b`.
5. Repeating steps 2, 3, and 4 until there are elements in `a` or as long as you do not have vertex to find.


<br>

### **Optimality**
---

This algorithm is optimal, meaning it always finds the best answer.

<br>

### **Implementation**
---

You can see an implementation of Dijkstra's Algorithm on a graph in the [`dijkstra.py`](./dijkstra.py) file, where each vertex contains a set of spatial coordinates and a list of neighbors. The distance between two vertices is returned by the heuristic function. We'll use a Priority Queue that is implemented with a Min-Heap to keep track of the vertex to visit.

> **Dijkstra**'s Implementation [dijkstra.py](./dijkstra.py)



<br>

### **Termination case**
---

After `v` iterations Dijkstra's will terminate, where `v` is the number of vertices in the graph.

To be correct, the Algorithm must correctly find the shortest path from one vertex to all others.


<br>

### **Time Complexity**
---
To determine the overall time complexity of this implementation of the Algorithm, we can analyze each step:
1. Initializing the auxiliary data structures is a constant-time operation;
2. Getting the current node from the heap can be done with worst-case time complexity of `O(log(V))`
4. Returning the value can happen in constant time but generally depends on the size of the path, which can never be more than `V`;
5. We need to check the cost to all the neighbors of the current vertex to update the priority queue, so this operation will be dependant on the number of edges `O(E)`;
6. Repeating steps 2, 3, and 4 until we have found the correct vertex means that we will need to extract the current vertex from a priority queue that in the worst-case contains all the vertices, an operation that can be done with time complexity of `O(log(V))`. In the worst-case scenario, this operation will be repeated `E` times.



As a result, the overall worst-case time complexity of this implementation of Dijkstra's Algorithm will be

<div align="center">

```
O(|V|) + O(|E| ⋅ log(|V|)) = O(|V| + |E|⋅log(|V|))

```

</div>


<br>

### **Space Complexity**
---

This Algorithm's implementation uses two auxiliary data structures, whose their length is proportional to the number of vertices. As a result, the Algorithm's space complexity will be `O(V)`.
