from math import comb


# Given: Positive integers n and m with 0≤m≤n≤2000
# Return: The sum of combinations C(n,k) for all k satisfying m≤k≤n, mod 1000000
def total_subsets(n, m):
    total = 1
    for k in range(m, n):
        total += comb(n, k)
        total %= 1000000
    return total


if __name__ == "__main__":
    nums = open("../data/rosalind_aspc.txt", "r").readline().split(' ')
    print(total_subsets(int(nums[0]), int(nums[1])))
