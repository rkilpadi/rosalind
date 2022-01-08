from Bio.SeqUtils import molecular_weight


# calculate mass of string representing amino acids
# Biopython adds weight of water molecule to its calculations (18.01056)
def get_mass(aas):
    return molecular_weight(aas, 'protein', monoisotopic=True) - 18.01056


if __name__ == "__main__":
    with open('data/rosalind_prtm.txt', 'r') as data:
        print(get_mass(data.read().rstrip()))
