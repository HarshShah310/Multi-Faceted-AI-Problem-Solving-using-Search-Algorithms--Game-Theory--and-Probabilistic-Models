class BayesianNetwork:
    def __init__(self):
        self.prob_Bt = 0.001
        self.prob_Bf = 1 - self.prob_Bt

        self.prob_Et = 0.002
        self.prob_Ef = 1 - self.prob_Et

        self.prob_J_given_At = 0.90
        self.prob_J_given_Af = 0.05

        self.prob_M_given_At = 0.70
        self.prob_M_given_Af = 0.01

        self.prob_A_given_Bt_and_Et = 0.95
        self.prob_A_given_Bt_and_Ef = 0.94
        self.prob_A_given_Bf_and_Et = 0.29
        self.prob_A_given_Bf_and_Ef = 0.001

    def parse_queries(self, query_list):
        parsed_queries = []
        if query_list is not None:
            parsed_queries.append(True if "Bt" in query_list else (False if "Bf" in query_list else None))
            parsed_queries.append(True if "Et" in query_list else (False if "Ef" in query_list else None))
            parsed_queries.append(True if "At" in query_list else (False if "Af" in query_list else None))
            parsed_queries.append(True if "Jt" in query_list else (False if "Jf" in query_list else None))
            parsed_queries.append(True if "Mt" in query_list else (False if "Mf" in query_list else None))
        return parsed_queries

    def calculate_probability(self, condition, c1, c2=None, c3=None):
        # Calculate conditional probability based on the given condition and values
        if condition == "B":
            return self.prob_Bt if c1 else self.prob_Bf
        elif condition == "E":
            return self.prob_Et if c1 else self.prob_Ef
        elif condition == "J|A":
            prob_t = self.prob_J_given_At if c2 else self.prob_J_given_Af
            return prob_t if c1 else 1 - prob_t
        elif condition == "M|A":
            prob_t = self.prob_M_given_At if c2 else self.prob_M_given_Af
            return prob_t if c1 else 1 - prob_t
        elif condition == "A|B,E":
            if c2 and c3:
                prob_t = self.prob_A_given_Bt_and_Et
            elif c2 and not c3:
                prob_t = self.prob_A_given_Bt_and_Ef
            elif not c2 and c3:
                prob_t = self.prob_A_given_Bf_and_Et
            else:
                prob_t = self.prob_A_given_Bf_and_Ef
            return prob_t if c1 else 1 - prob_t

    def calculate_joint_probability(self, queries_results):
        # Calculate the joint probability of all events
        p1 = self.calculate_probability("B", queries_results[0])
        p2 = self.calculate_probability("E", queries_results[1])
        p3 = self.calculate_probability("A|B,E", queries_results[2], queries_results[0], queries_results[1])
        p4 = self.calculate_probability("J|A", queries_results[3], queries_results[2])
        p5 = self.calculate_probability("M|A", queries_results[4], queries_results[2])
        return p1 * p2 * p3 * p4 * p5

    def calculate_probability_given_queries(self, queries_results):
        # Calculate the probability given the parsed queries
        if None in queries_results:
            # Handle cases where queries have missing values
            true_queries_results = list(queries_results)
            none_index = true_queries_results.index(None)
            true_queries_results[none_index] = True
            true_prob = self.calculate_probability_given_queries(true_queries_results)

            false_queries_results = list(queries_results)
            false_queries_results[none_index] = False
            false_prob = self.calculate_probability_given_queries(false_queries_results)

            return true_prob + false_prob
        else:
            return self.calculate_joint_probability(queries_results)

def main():
    import sys

    args_length = len(sys.argv)
    given_state = False
    arguments = []
    queries = []
    observations = []

    for i in range(1, args_length):
        arguments.append(sys.argv[i])

    if len(arguments) < 2 or len(arguments) > 6:
        print("Wrong number of arguments. Please provide valid input.")

    else:
        bayesian_network = BayesianNetwork()

        for argument in arguments:
            if argument == "given":
                given_state = True

            queries.append(argument)

            if given_state:
                observations.append(argument)

        if queries:
            num = bayesian_network.calculate_probability_given_queries(bayesian_network.parse_queries(queries))

            if observations:
                den = bayesian_network.calculate_probability_given_queries(bayesian_network.parse_queries(observations))

            else:
                den = 1

            print("Probability = %.10f" % (num / den))
        else:
            print("Error: Invalid query string")


if __name__ == '__main__':
    main()