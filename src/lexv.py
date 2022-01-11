from src import lexf


# assign lexicographic value for sorting
def assign_value(word):
    ret = []
    for letter in word:
        ret.append(alphabet_dict[letter])
    return ret


# every possible substring of alphabet of size n
def get_kmers(alphabet, n):
    result = []
    for i in range(n+1):
        result += lexf.get_kmers(alphabet, i)
    result.sort(key=assign_value)
    return result


if __name__ == "__main__":
    with open('../data/rosalind_lexv.txt', 'r') as data:
        lines = data.readlines()
        alphabet = lines[0].rsplit()
        # define lexicographic order in dictionary
        alphabet_dict = {}
        for i, letter in enumerate(alphabet):
            alphabet_dict[letter] = i
        kmers = get_kmers(alphabet, int(lines[1]))
        for k in kmers:
            print(k)
