import sys
from queue import PriorityQueue

class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def expand(self, connections):
        return [self.child_node(connection) for connection in connections.get(self.state, [])]

    def child_node(self, connection):
        next_state, cost = connection
        return Node(next_state, self, (self.state, next_state), self.path_cost + cost)

    def path(self):
        node, path_back = self, []
        while node:
            path_back.append(node.state)
            node = node.parent
        return list(reversed(path_back))
    
    # Define less than method to compare nodes based on path cost
    def __lt__(self, other):
        return self.path_cost < other.path_cost

def find_route(input_filename, origin_city, destination_city, heuristic_filename=None):
    connections = {}
    with open(input_filename) as f:
        for line in f:
            if line.strip() == 'END OF INPUT':
                break
            source, dest, cost = line.split()
            cost = float(cost)
            connections.setdefault(source, []).append((dest, cost))
            connections.setdefault(dest, []).append((source, cost))

    heuristic = {}
    if heuristic_filename:
        with open(heuristic_filename) as f:
            for line in f:
                if line.strip() == 'END OF INPUT':
                    break
                city, h_value = line.split()
                heuristic[city] = float(h_value)

    start_node = Node(origin_city)
    goal_test = lambda state: state == destination_city

    fringe = PriorityQueue()
    fringe.put((0, start_node))
    closed_set = set()

    # Variables to keep track of node counts
    nodes_popped = 0
    nodes_expanded = 0
    nodes_generated = 1  # Start with the initial node

    while not fringe.empty():
        _, node = fringe.get()
        nodes_popped += 1

        if goal_test(node.state):
            route = node.path()
            distance = node.path_cost
            return route, distance, nodes_popped, nodes_expanded, nodes_generated, connections

        if node.state not in closed_set:
            closed_set.add(node.state)
            nodes_expanded += 1

            for child in node.expand(connections):
                nodes_generated += 1
                if heuristic:
                    h = heuristic[child.state]
                    f = child.path_cost + h
                    fringe.put((f, child))
                else:
                    fringe.put((child.path_cost, child))

    return None, float('inf'), nodes_popped, nodes_expanded, nodes_generated, connections

def main():
    if len(sys.argv) < 4:
        print("Usage: find_route input_filename origin_city destination_city [heuristic_filename]")
        return

    input_filename = sys.argv[1]
    origin_city = sys.argv[2]
    destination_city = sys.argv[3]
    heuristic_filename = None
    if len(sys.argv) > 4:
        heuristic_filename = sys.argv[4]

    route, distance, nodes_popped, nodes_expanded, nodes_generated, connections = find_route(input_filename, origin_city, destination_city, heuristic_filename)

    if route:
        print("Nodes Popped:", nodes_popped)
        print("Nodes Expanded:", nodes_expanded)
        print("Nodes Generated:", nodes_generated)
        print("Distance: {:.1f} km".format(distance))
        print("Route:")
        for i in range(len(route) - 1):
            city1 = route[i]
            city2 = route[i+1]
            cost = None
            for dest, c in connections[city1]:
                if dest == city2:
                    cost = c
                    break
            if cost is not None:
                print("{} to {}, {:.1f} km".format(city1, city2, cost))
            else:
                print("Connection not found between {} and {}".format(city1, city2))
    else:
        print("Nodes Popped:", nodes_popped)
        print("Nodes Expanded:", nodes_expanded)
        print("Nodes Generated:", nodes_generated)
        print("Distance: infinity")
        print("Route:")
        print("None")

if __name__ == "__main__":
    main()