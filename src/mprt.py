from Bio import SeqIO
from io import StringIO
from urllib.request import urlopen


# Given: At most 15 UniProt Protein Database access IDs.
# Return: For each protein possessing the N-glycosylation motif N{P}[ST]{P},
# output its given access ID followed by a list of locations in the protein string
def find_n_glycosylation(protein):
    locations = []
    for i in range(len(protein)-3):
        if protein[i] == 'N' and protein[i+1] != 'P' and \
                (protein[i+2] == 'S' or protein[i+2] == 'T') and protein[i+3] != 'P':
            locations.append(i+1)
    return locations


if __name__ == "__main__":
    with open('../data/rosalind_mprt.txt', 'r') as data, open('../results/mprt_results.txt', 'w') as output:
        for uniprot in data:
            url = 'https://www.uniprot.org/uniprot/' + uniprot.rstrip() + '.fasta'
            content_io = StringIO(urlopen(url).read().decode('utf8'))
            record = list(SeqIO.parse(content_io, 'fasta'))[0]
            motifs_found = find_n_glycosylation(record.seq)
            if motifs_found:
                output.write(uniprot.rstrip() + '\n')
                output.write(' '.join(map(str, motifs_found)) + '\n')
        output.close()
