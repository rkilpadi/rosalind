# reverses a DNA sequence and returns its complement
def dna_complement(dna):
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
    return complement[::-1]


if __name__ == "__main__":
    with open('../data/rosalind_revc.txt', 'r') as data:
        print(dna_complement(data.read()))
