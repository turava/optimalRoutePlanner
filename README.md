# Optimal Route Planner

## Overview
The **Optimal Route Planner** is a Python program designed to find the most efficient routes in a transportation network modeled as a **weighted, directed graph**. It uses **graph theory algorithms** to compute the shortest path and up to three alternative paths between two points (nodes). This tool is particularly suited for scenarios such as urban transportation planning, logistics, or any application that requires optimal route selection.

---

## Features
- **Graph Representation**: Supports a weighted, directed graph, where:
  - Nodes represent cities, intersections, or locations.
  - Edges represent routes with a weight (distance or cost).
- **Shortest Path Calculation**: Implements Dijkstra’s algorithm using a custom min-heap to find the shortest path between two nodes.
- **Alternative Routes**: Finds the second and third shortest routes, providing redundancy and options.
- **Dynamic Input**: Allows the user to input a starting and destination city.
- **Error Handling**: Provides meaningful feedback when no route is found or the graph lacks connectivity.
- **Custom Min-Heap**: Uses a custom implementation of a priority queue, avoiding the need for external libraries.

---

## How It Works
1. **Input Graph**: The graph is represented as a list of edges (tuples), where each edge includes:
   - The starting node (e.g., "Minsk").
   - The ending node (e.g., "Berlin").
   - The weight of the edge (e.g., distance or cost).

2. **Algorithm**: 
   - Dijkstra's algorithm is used to calculate the shortest paths.
   - A custom `MinHeap` is implemented to manage the priority queue.

3. **User Interaction**: 
   - The user enters the starting city and destination city.
   - The program computes and displays the shortest route and any alternative routes, if they exist.

4. **Output**: 
   - If a route exists, it outputs the path and total distance.
   - If no route exists, it informs the user to check the graph's connectivity.

---

## Example Graph
The graph is hardcoded in the program. Below is an example graph used in the code:

```python
edges = [
    ('Minsk', 'Berlin', 10),  # Direct route
    ('Minsk', 'Warsaw', 6),  # Indirect route
    ('Warsaw', 'Berlin', 3),  # Route from Warsaw to Berlin
    ('Berlin', 'Paris', 8),  # Extra connections
    ('Paris', 'Barcelona', 5)
]
