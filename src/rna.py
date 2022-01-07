# takes in a sequence of DNA and returns a sequence of RNA
def to_rna(filename):
    with open(filename, "r") as data:
        dna = data.read().rstrip()
    print(dna.replace('T', 'U'))


to_rna('data/rosalind_dna.txt')
