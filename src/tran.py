from Bio import SeqIO


def transition_transversion_ratio(seq1, seq2):
    transitions, transversions = 0, 0
    transitions_set1 = ['A', 'G']
    transitions_set2 = ['C', 'T']
    for nuc1, nuc2 in zip(seq1, seq2):
        if nuc1 != nuc2:
            if nuc1 in transitions_set1 and nuc2 in transitions_set1:
                transitions += 1
            elif nuc1 in transitions_set2 and nuc2 in transitions_set2:
                transitions += 1
            else:
                transversions += 1
    return transitions/transversions


if __name__ == "__main__":
    records = list(SeqIO.parse('data/rosalind_tran.txt', 'fasta'))
    print(transition_transversion_ratio(records[0].seq, records[1].seq))
