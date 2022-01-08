# Returns all locations of substring within a string
def find_motifs(filename):
    with open(filename, 'r') as data:
        lines = data.read().splitlines()
    string = lines[0]
    substring = lines[1]

    i, j = 0, len(substring)
    while j < len(string):
        if string[i:j] == substring:
            print(i+1)
        i += 1
        j += 1


find_motifs('data/rosalind_subs.txt')
