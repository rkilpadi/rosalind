# counts nucleotides and returns four integers representing A, C, G, T
def count_bases(filename):
    with open(filename, "r") as data:
        dna = data.read().rstrip()

    a, c, g, t = 0, 0, 0, 0
    for A in dna:
        a += 1
    for C in dna:
        c += 1
    for G in dna:
        g += 1
    for T in dna:
        t += 1
    print(a, c, g, t)


count_bases('data/rosalind_dna.txt')
