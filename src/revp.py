from Bio import SeqIO
from src import revc


# Return: The position and length of every reverse palindrome between length 4 and 12
# For instance, GCATGC is a reverse palindrome because its reverse complement is GCATGC
def reverse_palindromes(dna, min_len, max_len):
    restriction_sites = []
    complement = revc.dna_complement(dna)  # used to verify substrings
    current = dna[:max_len]  # substring being tested
    i = 0
    while i < len(dna) - min_len:
        # shrink current by 2 until min_len is reached, then increment index and repeat
        if len(current) >= min_len:
            if current == complement[len(dna) - i - len(current):len(dna) - i]:
                restriction_sites.append((i+1, len(current)))  # counts from 1
            current = dna[i:i+len(current)-2]
        else:
            i += 1
            current = dna[i:i + max_len]
            # ensure substrings are of even length (must be even to pass)
            if len(current) % 2 != 0:
                current = current[:-1]
    return restriction_sites


if __name__ == "__main__":
    seq = list(SeqIO.parse('../data/test.txt', 'fasta'))[0].seq
    for restriction_site in reverse_palindromes(str(seq), 4, 12):
        print(str(restriction_site[0]) + ' ' + str(restriction_site[1]))
