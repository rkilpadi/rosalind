# Given: A positive integer n
# Return: The total number of subsets of {1,2,…,n} modulo 1,000,000
# answer is simply 2^n, each number can be either present or absent
def total_subsets(n):
    total = 1
    for i in range(n):
        total *= 2
        total %= 1000000
    return total


if __name__ == "__main__":
    print(total_subsets(int(open("../data/rosalind_sset.txt", "r").read())))

