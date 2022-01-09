from Bio import SeqIO


# Given: A collection of DNA strings in FASTA format having total length at most 10 kbp
# Return: The adjacency list corresponding to O3 (k = 3)
# s has an edge to t if s has a suffix of length k that matches t's prefix of length k
def overlap_graph(records, k):
    result = ''
    for s in records:
        for t in records:
            if s is not t and s.seq[-k:] == t.seq[:k]:
                result += s.id + ' ' + t.id + '\n'
    return result


if __name__ == "__main__":
    print(overlap_graph(list(SeqIO.parse('../data/rosalind_grph.txt', 'fasta')), 3))
