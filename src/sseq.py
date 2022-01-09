from Bio import SeqIO


# Given two strings, returns the indices of a subsequence of the second string within the first
# A subsequence is a collection of symbols contained in order (though not necessarily contiguously)
def find_subsequence(string, sub):
    seq_idx, string_idx = 0, 0
    indices = []
    for char in string:
        if char == sub[seq_idx]:
            indices.append(string_idx)
            seq_idx += 1
            if seq_idx >= len(sub):
                break
        string_idx += 1
    return indices


if __name__ == '__main__':
    records = list(SeqIO.parse('../data/rosalind_sseq.txt', 'fasta'))
    vals = find_subsequence(records[0].seq, records[1].seq)
    for val in vals:
        print(val+1)
