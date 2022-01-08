# transcribes DNA to RNA
def transcribe(filename):
    with open(filename, "r") as data:
        dna = data.read().rstrip()

    print(dna.replace('T', 'U'))


transcribe('data/rosalind_dna.txt')
