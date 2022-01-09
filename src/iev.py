# Given: Six integers correspond to the number of couples in a population possessing each genotype
# In order, the six given integers represent the number of couples having the following genotypes:
# AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa-aa, aa-aa
# Return: The expected number of offspring displaying the dominant phenotype in the next generation
# each set of parents has 2 offspring
def avg_dominant(genotype_counts):
    avg = genotype_counts[0] + genotype_counts[1] + genotype_counts[2]
    avg += genotype_counts[3] * 3/4
    avg += genotype_counts[4] * 1/2
    return avg * 2


if __name__ == "__main__":
    with open('../data/rosalind_iev.txt', 'r') as data:
        nums = list(map(int, data.readline().split(' ')))
        print(avg_dominant(list(map(int, nums))))
