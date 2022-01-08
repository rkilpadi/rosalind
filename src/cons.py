from Bio import SeqIO


# creates a list with n 0s
def populate_list(n):
    return [0 for i in range(n)]


# given a list of sequences, returns a sequence of most common nucleotides
# and a matrix of counts for where each occurred
def get_consensus(dna_records):
    size = len(dna_records[0].seq)
    a_counts = populate_list(size)
    c_counts = populate_list(size)
    g_counts = populate_list(size)
    t_counts = populate_list(size)
    consensus = ''

    # add to count for each position
    for record in dna_records:
        for i, nuc in enumerate(record.seq):
            if nuc == 'A':
                a_counts[i] += 1
            if nuc == 'C':
                c_counts[i] += 1
            if nuc == 'G':
                g_counts[i] += 1
            if nuc == 'T':
                t_counts[i] += 1

    # find the most common nucleotide for each position
    for i in range(size):
        max_count = max(a_counts[i], c_counts[i], g_counts[i], t_counts[i])
        if max_count == a_counts[i]:
            consensus += 'A'
        elif max_count == c_counts[i]:
            consensus += 'C'
        elif max_count == g_counts[i]:
            consensus += 'G'
        elif max_count == t_counts[i]:
            consensus += 'T'

    return consensus, a_counts, c_counts, g_counts, t_counts


if __name__ == "__main__":
    records = list(SeqIO.parse('data/rosalind_cons.txt', 'fasta'))
    results = get_consensus(records)
    f = open('results/cons_results.txt', 'w')
    f.write(results[0] + '\n')
    f.write('A: ' + ' '.join(str(val) for val in results[1]) + '\n')
    f.write('C: ' + ' '.join(str(val) for val in results[2]) + '\n')
    f.write('G: ' + ' '.join(str(val) for val in results[3]) + '\n')
    f.write('T: ' + ' '.join(str(val) for val in results[4]) + '\n')
    f.close()
