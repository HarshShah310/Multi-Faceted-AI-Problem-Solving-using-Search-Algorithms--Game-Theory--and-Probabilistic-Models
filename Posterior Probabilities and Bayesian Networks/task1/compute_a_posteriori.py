bags_priors = [0.1, 0.2, 0.4, 0.2, 0.1]
cherry_prob = [1.0, 0.75, 0.50, 0.25, 0.0]
lime_prob = [0.0, 0.25, 0.50, 0.75, 1.0]

import sys

def compute_a_posteriori():
    arg_length = len(sys.argv)

    if arg_length != 2:
        print("Incorrect number of arguments. Please provide a sequence of observations.")
        return

    obs_str = sys.argv[1].upper()  # Convert the input to uppercase to handle lowercase input
    obs_count = len(obs_str)
    result_file_obj = open("result.txt", "w")

    wrt_ls = []
    wrt_ls.append("Observation sequence Q: " + obs_str)
    wrt_ls.append("Length of Q: " + str(obs_count))

    bag_prob = [p for p in bags_priors]

    for i in range(obs_count):
        wrt_ls.append("\nAfter Observation " + str(i + 1) + " = " + obs_str[i] + ":\n")

        sum_cherry = sum(bag_prob[j] * cherry_prob[j] for j in range(5))
        sum_lime = sum(bag_prob[j] * lime_prob[j] for j in range(5))

        if obs_str[i] == "C":
            for j in range(5):
                bag_prob[j] = (bag_prob[j] * cherry_prob[j]) / sum_cherry
                wrt_ls.append("P(h" + str(j + 1) + " | Q) = " + str(bag_prob[j]))
        elif obs_str[i] == "L":
            for j in range(5):
                bag_prob[j] = (bag_prob[j] * lime_prob[j]) / sum_lime
                wrt_ls.append("P(h" + str(j + 1) + " | Q) = " + str(bag_prob[j]))

        # Calculate the probabilities of picking cherry or lime candies after each observation
        sum_cherry = sum(bag_prob[j] * cherry_prob[j] for j in range(5))
        sum_lime = sum(bag_prob[j] * lime_prob[j] for j in range(5))
        wrt_ls.append("\nProbability that the next candy we pick will be C, given Q: " + str(sum_cherry))
        wrt_ls.append("Probability that the next candy we pick will be L, given Q: " + str(sum_lime))

    result_file_obj.write('\n'.join(wrt_ls))
    result_file_obj.close()

if __name__ == '__main__':
    compute_a_posteriori()