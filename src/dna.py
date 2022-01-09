# counts nucleotides and returns four integers representing A, C, G, T
def count_bases(dna):

    a, c, g, t = 0, 0, 0, 0
    for A in dna:
        a += 1
    for C in dna:
        c += 1
    for G in dna:
        g += 1
    for T in dna:
        t += 1
    return a, c, g, t


if __name__ == "__main__":
    with open('../data/rosalind_dna.txt') as data:
        print(count_bases(data.read().rstrip()))
