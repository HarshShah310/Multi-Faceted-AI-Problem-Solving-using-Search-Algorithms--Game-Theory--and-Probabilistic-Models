Harsh Shah (1002057387)
----------------------------------
Programming Language: Python 3.12.2
---------------------------------------------------
Code Structure:

1. Import Statement:
Imports the sys module for handling command-line arguments.

2. Class Definition: BayesianNetwork:
Constructor __init__: Initializes the probabilities for different events in the Bayesian network.
Method parse_queries: Parses the query string to determine the events to query for.
Method calculate_probability: Calculates the probability based on the given condition and values.
Method calculate_joint_probability: Calculates the joint probability of all events.
Method calculate_probability_given_queries: Calculates the probability given the parsed queries.

3. Main Block:
Parses command-line arguments to extract the query strings.
Creates an instance of the BayesianNetwork class.
Calls methods to calculate probabilities based on the provided queries.
Prints the resulting probability.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
How to run the code:

1. Open the command prompt and use the cd command to change the current directory to the directory that contains the code file bnet.py and then use the following commands:
python bnet.py <query_arguments>
For example: python bnet.py Bt Af given Mf

2. The script will calculate the probability based on the provided queries and print the result.