import scan


# counts nucleotides and returns four integers representing A, C, G, T
def count_bases(data):
    gene = scan.scan_gene(data)
    a, c, g, t = 0, 0, 0, 0
    for char in gene:
        match char:
            case 'A':
                a += 1
            case 'C':
                c += 1
            case 'G':
                g += 1
            case 'T':
                t += 1
    print(a, c, g, t)


if __name__ == '__main__':
    count_bases("data/rosalind_dna.txt")
