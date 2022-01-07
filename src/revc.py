# reverses a DNA sequence and returns its complement
def dna_complement(filename):
    with open(filename, "r") as data:
        dna = data.read().rstrip()

    complement = ''
    for char in dna:
        if char == 'A':
            complement += 'T'
        if char == 'T':
            complement += 'A'
        if char == 'C':
            complement += 'G'
        if char == 'G':
            complement += 'C'
    print(complement[::-1])


dna_complement('data/rosalind_revc.txt')