class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        """Push an item onto the heap."""
        self.heap.append(item)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        """Pop the smallest item off the heap."""
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return root

    def _sift_up(self, index):
        """Ensure heap property from child to parent."""
        parent = (index - 1) // 2
        if parent >= 0 and self.heap[index][0] < self.heap[parent][0]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._sift_up(parent)

    def _sift_down(self, index):
        """Ensure heap property from parent to child."""
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left][0] < self.heap[smallest][0]:
            smallest = left
        if right < len(self.heap) and self.heap[right][0] < self.heap[smallest][0]:
            smallest = right
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._sift_down(smallest)

    def is_empty(self):
        """Check if the heap is empty."""
        return len(self.heap) == 0


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))

    def dijkstra(self, start, end):
        pq = MinHeap()
        pq.push((0, start, [start]))
        visited = set()

        shortest_paths = []

        while not pq.is_empty():
            dist, current, path = pq.pop()

            if current in visited:
                continue
            visited.add(current)

            if current == end:
                shortest_paths.append((dist, path))
                if len(shortest_paths) == 3:  # Stop after finding three shortest paths
                    return shortest_paths

            for neighbor, weight in self.graph.get(current, []):
                if neighbor not in visited:
                    pq.push((dist + weight, neighbor, path + [neighbor]))

        return shortest_paths if shortest_paths else None

    def print_routes(self, routes):
        if not routes:
            print("No route found.")
        else:
            for i, (dist, path) in enumerate(routes, 1):
                print(f"{i}. Route: {' -> '.join(path)} with total distance {dist}")


def main():
    # Create graph instance
    city_graph = Graph()

    # Example graph input with connections
    edges = [
        ('Minsk', 'Berlin', 10),  # Direct route
        ('Minsk', 'Warsaw', 6),  # Indirect route
        ('Warsaw', 'Berlin', 3),  # Route from Warsaw to Berlin
        ('Berlin', 'Paris', 8),  # Extra connections
        ('Paris', 'Barcelona', 5)
    ]

    # Adding edges to the graph
    for u, v, weight in edges:
        city_graph.add_edge(u, v, weight)

    # Debug: Print the graph structure
    print("Graph Structure:", city_graph.graph)

    # User input for origin and destination
    origin = input("Enter the starting city: ").strip().title()
    destination = input("Enter the destination city: ").strip().title()

    # Calculate the shortest paths
    routes = city_graph.dijkstra(origin, destination)

    # Print results
    if not routes:
        print(f"No route found from {origin} to {destination}. Please check the graph for connectivity.")
    else:
        city_graph.print_routes(routes)


if __name__ == "__main__":
    main()
