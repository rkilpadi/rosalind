from Bio.Seq import Seq


# translates RNA to protein sequence
def translate(filename):
    with open(filename, 'r') as data:
        rna = Seq(data.read().rstrip())

    print(rna.translate(to_stop=True))


translate('data/rosalind_prot.txt')
