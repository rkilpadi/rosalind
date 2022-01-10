# Given: Positive integers n and k
# Return: The total number of partial permutations P(n,k), modulo 1000000.
def partial_permutations(n, k):
    total = 1
    for i in range(k):  # i = items chosen already
        total *= n - i  # multiply by items left to choose
        total %= 1000000
    return total


if __name__ == "__main__":
    with open('../data/rosalind_pper.txt', 'r') as data:
        nums = data.readline().split(' ')
        print(partial_permutations(int(nums[0]), int(nums[1])))
