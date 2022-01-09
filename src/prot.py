from Bio.Seq import Seq


# translates RNA to protein sequence
def translate(rna):
    return rna.translate(to_stop=True)


if __name__ == "__main__":
    with open('../data/rosalind_prot.txt', 'r') as data:
        print(translate(Seq(data.read().rstrip())))
