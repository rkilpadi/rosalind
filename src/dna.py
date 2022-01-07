import scan


# counts nucleotides and returns four integers representing A, C, G, T
def count_bases(data):
    gene = scan.scan_gene(data)
    a, c, g, t = 0, 0, 0, 0
    for A in gene:
        a += 1
    for C in gene:
        c += 1
    for G in gene:
        g += 1
    for T in gene:
        t += 1
    print(a, c, g, t)


if __name__ == '__main__':
    count_bases("/Users/rkilpadi/Documents/GitHub/rosalind/data/rosalind_dna.txt")
