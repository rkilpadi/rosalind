# Given: A positive integer n (3≤n≤10000)
# Return: The number of internal nodes of any unrooted binary tree having n leaves
# start with base case of 3 nodes. This tree has 2 leaves and 0 internal leaves.
# from there, one internal node is created for every new leaf, so the answer is simply n-2
if __name__ == "__main__":
    print(int(open("../data/rosalind_inod.txt", "r").read())-2)
