# Returns all locations of substring within a string
def find_motifs(string, substring):
    occurrences = []
    i, j = 0, len(substring)
    while j < len(string):
        if string[i:j] == substring:
            occurrences.append(i+1)
        i += 1
        j += 1
    return occurrences


if __name__ == "__main__":
    with open('data/rosalind_subs.txt', 'r') as data:
        lines = data.read().splitlines()
        print(find_motifs(lines[0], lines[1]))
