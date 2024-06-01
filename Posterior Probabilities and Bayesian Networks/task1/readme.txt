Harsh Shah (1002057387)
----------------------------------
Programming Language: Python 3.12.2
---------------------------------------------------
Code Structure:

1. Initialization:
bags_priors: Prior probabilities of selecting each bag.
cherry_prob: Probabilities of picking a cherry candy from each bag.
lime_prob: Probabilities of picking a lime candy from each bag.

2. Import Statement:
import sys: Importing the sys module to access command-line arguments.

3. Function Definition:
compute_a_posteriori(): The main function responsible for computing posterior probabilities based on observations. It first checks if the correct number of arguments is provided via the command line. Then, it processes the sequence of observations, updating the probabilities of selecting each bag after each observation. It also calculates the probabilities of picking a cherry or a lime candy after each observation. The results are written to a file named "result.txt".

4. Main Block:
Checks if the script is being run directly. If so, calls the compute_a_posteriori() function to start the computation.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
How to run the code:

1. Open the command prompt and use the cd command to change the current directory to the directory that contains the code file compute_a_posteriori.py and then use the following commands:
python compute_a_posteriori.py <observation_sequence>
For example: python compute_a_posteriori.py CLLCCCLLL	(with observations)
		      python compute_a_posteriori.py	(without any observations)

2. After running the script, it will generate a file named result.txt in the same directory. Open this file to view the results.