# A* Algorithm

An informed search algorithm that uses some additional information to determine its best next move. <br/>

This additional information is calculated in this case by a function. 

<div align="center"> 

$f(n)=g(n)+h(n)$  

</div>

- where $n$ is the next vertex, $g(n)$ is the cost to get from the start vertex to the next, 
- and $h(n)$ is a heuristic function that approximates the cost to get from $n$ to the vertex to find
- and never overestimates the actual cost between $n$ and the vertex to find. 
- The Algorithm will then pick its next move based on which one has the lowest value of $f(n)$.




<br>

### **Algorithm's workflow**
---
1. Initialize some additional data structures to keep track of: the vertices to visit (starting from the starting vertex); from which adjacent vertex a vertex has been visited (None for the starting vertex); and the cost to get from the starting vertex to that one (0 for the starting vertex). We will call these data structures $a$, $b$, and $c$ respectively for simplicity;
2. Set the current vertex to be the one with the lowest value of $f(n)$ in $a$ and remove it from $a$;
3. If the current vertex is the vertex to find, reconstruct and return the path to that vertex;
4. Otherwise, for each of its neighbors $n$, calculate $g(n)$ and if they are not in $c$, or if they are but this new value of $g(n)$ is lower than the previous one: updates its value in $c$, add it to $a$ with priority $f(n)$, and set it as visited from the current node in $b$.
5. Repeat steps 2, 3, and 4 until there are elements in $a$ or as long as you do not have found the vertex to find.

<br>

### **Optimality**
---

This Algorithm is optimal, which means that it will always find the best solution.


<br>

### **Implementation**
---

In the following `astra.py` file, yo ucan see implementation of the A* algorithm on a graph where each vertex has a set of spatial coordinates and a list of neighbors, and the heuristic function returns the distance between 2 vertices. To keep track of the vertex to visit, we will use a Priority Queue implemented with a Min-Heap.


> A*'s Implementation [astra.py](./astar.py)


---

<br>

### **Termination case**
---
☑️
For each input, this Algorithm will terminate, either because it finds the shortest path to a vertex or because there are no more items to visit and no path exists.

<br>

### **Correctness**
---

If this algorithm can discover the shortest path between two vertices in a graph, then it is correct.

<br>

### **Time Complexity**
---

A* time complexity depends on the number of vertices that need to be visited before finding the vertex that we were looking for and thus on the efficiency of the heuristic function.

- With an uninformative heuristic function, this Algorithm will behave like Dijkstra's Algorithm and potentially visit every vertex and edge in the graph, an operation with time complexity of $O(|V|+|E|)$. 
- This time complexity can also be expressed as $O(b^{d})$, where $b$ is the average number of adjacent vertices and $d$ is the number of edges between the starting node and the node to find.
- In the best case for this Algorithm, the heuristic function is so efficient that only the nodes in the path between the two vertices are ever explored, its time complexity, in this case, will be $Ω(d)$, where $d$ is the number of edges between the two nodes.


<br>

### **Space Complexity**
---

Because this algorithm keeps track of all the vertices it visits, its space complexity will be $O(V)$ in the worst case.