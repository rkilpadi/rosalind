from Bio import SeqIO


# Given: A collection DNA strings
# Return: A longest common substring of the collection
def longest_substring(dnas):
    longest = ''
    smallest_seq = min(dnas, key=len)
    # generate all substrings of smallest seq and check whether universal
    for i in range(len(smallest_seq)):
        # stop when remaining substrings smaller than longest so far
        if len(smallest_seq) - i <= len(longest):
            break
        for j in range(i, len(smallest_seq)):
            motif = smallest_seq[i:j+1]
            # skip if motif smaller than longest
            if len(motif) <= len(longest):
                continue
            # otherwise, check if motif is shared and update longest if true
            elif verify_motif(motif, dnas):
                longest = motif
    return longest


# check if motif is shared among all strings
def verify_motif(motif, dnas):
    for dna in dnas:
        if motif not in dna:
            return False
    return True


if __name__ == '__main__':
    records = list(SeqIO.parse('../data/rosalind_lcsm.txt', 'fasta'))
    seqs = []
    for record in records:
        seqs.append(str(record.seq))
    print(longest_substring(seqs))
