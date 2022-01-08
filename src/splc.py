from Bio import SeqIO
from src import subs
from src import prot


# inputs RNA Seq and intron Seqs, splices and translates RNA
def splice(rna, intron_records):
    spliced_rna = rna
    for intron in intron_records:
        found_idx = subs.find_motifs(str(spliced_rna), str(intron.seq))[0]
        spliced_rna = spliced_rna[:found_idx-1] + spliced_rna[found_idx+len(intron)-1:]
    return prot.translate(spliced_rna)


if __name__ == "__main__":
    records = list(SeqIO.parse('data/rosalind_splc.txt', 'fasta'))
    print(splice(records.pop(0).seq, records))
