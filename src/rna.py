import scan


# takes in a sequence of DNA and returns a sequence of RNA
def to_rna(data):
    print(scan.scan_gene(data).replace('T', 'U'))


to_rna('data/rosalind_dna.txt')
