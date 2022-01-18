from math import log10


# Given: A DNA string s and an array A containing GC-contents
# Return: An array B having the same length as A in which B[k]
# represents the common logarithm of the probability that a random string
# constructed with the GC-content found in A[k] will match s exactly.
def get_probabilities(dna, gcs):
    probabilities = [1] * len(gcs)
    for nucleotide in dna:
        for i, gc in enumerate(gcs):
            if nucleotide == 'G' or nucleotide == 'C':
                probabilities[i] *= gc/2  # probability of one of G or C
            else:
                probabilities[i] *= (1-gc)/2  # probability of one of A or T
    return list(map(log10, probabilities))


if __name__ == '__main__':
    with open('../data/rosalind_prob.txt', 'r') as data:
        lines = data.readlines()
        s = lines[0].rstrip()
        A = list(map(float, lines[1].rstrip().split(' ')))
        print(*get_probabilities(s, A))
