Harsh Shah (1002057387)
----------------------------------
Programming Language: Python 3.11
------------------------------------------------
Code Structure:

Import Statements: It begins with importing necessary modules. sys module is imported to access command-line arguments, and PriorityQueue class is imported from the queue module.

Node Class: Defines a class named Node. Each node represents a state in the search space. It has attributes such as state, parent, action, and path_cost. It also contains methods for expanding the node, generating child nodes, and retrieving the path from the root node.

find_route Function: Defines the main search function find_route, which takes input parameters including filenames, origin city, destination city, and optionally a heuristic filename. It reads the input files, initializes necessary data structures, performs the search using algorithm, and returns the route, distance, and various node counts.

main Function: The entry point of the program. It checks command-line arguments, calls the find_route function with appropriate parameters, and prints the results.

Execution Block: Checks if the script is run directly (__name__ == "__main__") and then calls the main() function.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
How to run the code:

Open the command prompt and use the cd command to change the current directory to the directory that contains the code file find_route.py and the input text files input1.txt and h_kassel.txt, and then use the following commands:
    
1. Optimal path using uninformed search (uniform cost search)

	python find_route.py {input file name} {start city} {goal city}

	i.e. python find_route.py input1.txt Bremen Kassel

2. Optimal path using informed search (A* search)

	python find_route.py {input file name} {start city} {goal city} {heuristic file name}

	i.e. python find_route.py input1.txt Bremen Kassel h_kassel.txt