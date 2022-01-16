from Bio import SeqIO
from Bio import Seq
from src.revc import dna_complement


# Given: A DNA string s
# Return: Every protein string that can be translated from ORFs of s
def orf_proteins(dna):
    frames = [dna, dna[1:], dna[2:], dna_complement(dna),
              dna_complement(dna[:-1]), dna_complement(dna[:-2])]
    proteins = set()
    for frame in frames:
        proteins.update(find_orfs(Seq.translate(frame)))
    return proteins


def find_orfs(aas):
    proteins = set()
    current_proteins = []  # list of ongiong protein strings
    started = False

    for aa in aas:
        if aa == 'M':  # start codon
            started = True
            current_proteins.append('')
        elif aa == '*':  # stop codon
            if started:
                proteins.update(current_proteins)
            started = False
            current_proteins = []
        if started:
            for i in range(len(current_proteins)):
                current_proteins[i] += aa
    return proteins


if __name__ == '__main__':
    records = SeqIO.parse('../data/rosalind_orf.txt', 'fasta')
    result = orf_proteins(list(records)[0].seq)
    print(*result)
