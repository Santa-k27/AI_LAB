
import heapq
import math

class Graph:
    def __init__(self):
        self.edges = {}

    def neighbors(self, node):
        return self.edges[node]

    def cost(self, from_node, to_node):
        return self.edges[from_node][to_node]

    def heuristic(self, node, goal):
        # Modify the heuristic method to work with node labels
        # For example, you can use a pre-computed heuristic dictionary
        heuristic_values = {'A': 5, 'B': 3, 'C': 8, 'D': 0}  # Replace with actual heuristic values
        return heuristic_values[node]

def astar(start, goal, graph):
    frontier = [(0, start)]
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while frontier:
        current = heapq.heappop(frontier)[1]

        if current == goal:
            break

        for next_node in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next_node)
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost + graph.heuristic(next_node, goal)
                heapq.heappush(frontier, (priority, next_node))
                came_from[next_node] = current

    return came_from, cost_so_far

def main():
    graph = Graph()
    graph.edges = {
        'A': {'B': 15, 'C': 10},
        'B': {'A': 15, 'C': 3, 'D': 15},
        'C': {'A': 1, 'B': 3, 'D': 5},
        'D': {'B': 5, 'C': 5}
    }
    start = 'A'
    goal = 'D'
    came_from, cost_so_far = astar(start, goal, graph)
   
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    path = path[::-1]
    print("Path:", path)
    print("Cost:", cost_so_far[goal])

if __name__ == "__main__":
    main()