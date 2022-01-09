# transcribes DNA to RNA
def transcribe(dna):
    return dna.replace('T', 'U')


if __name__ == "__main__":
    with open('../data/rosalind_rna.txt', 'r') as data:
        print(transcribe(data.read()))
