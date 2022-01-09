# Given: Three positive integers k, m, and n, k individuals are homozygous dominant
# for a factor, m are heterozygous, and n are homozygous recessive.
# Return: The probability that two randomly selected mating organisms
# will produce an individual possessing a dominant allele
def dominant_probability(k, m, n):
    population = k + m + n
    # chance of at least one k parent (dominant offspring guaranteed)
    probability = 1-(1-k/population)*(population-1-k)/(population-1)
    # chance of 2 m parents that produce dominant offspring
    probability += m/population * (m-1)/(population-1) * 3/4
    # chance of 1 m, 1 n parent that produce dominant offspring
    probability += m/population * n/(population-1) * 1/2
    probability += n/population * m/(population-1) * 1/2
    return probability


if __name__ == "__main__":
    with open('data/rosalind_iprb.txt', 'r') as data:
        nums = data.readline().split(' ')
        print(dominant_probability(int(nums[0]), int(nums[1]), int(nums[2])))
