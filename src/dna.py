import scan


# counts nucleotides and returns four integers representing A, C, G, T
def count_bases(data):
    dna = scan.scan_gene(data)
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


if __name__ == '__main__':
    count_bases("data/rosalind_dna.txt")
