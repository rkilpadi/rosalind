# add 1 to number represented by list of digits in base n
# each digit represents a symbol in an alphabet of size n
# returns empty list when increment would require more digits than size of list
def increment(l, n):
    if not l:
        return
    if l[-1] == n - 1:
        new = increment(l[:-1], n)
        if not new:
            return []
        new.append(0)
        return new
    l[-1] += 1
    return l


# Given: A collection symbols defining an ordered alphabet and a positive integer n
# Return: All ordered strings of length n that can be formed from the alphabet
def get_kmers(alphabet, n):
    result = []
    indices = [0 for _ in range(n)]  # which symbols to add next
    while indices:
        to_add = ''
        for idx in indices:
            to_add += alphabet[idx]
        result.append(to_add)
        indices = increment(indices, len(alphabet))
    return result


if __name__ == "__main__":
    with open('../data/rosalind_lexf.txt', 'r') as data:
        lines = data.readlines()
        kmers = get_kmers(lines[0].rsplit(), int(lines[1]))
        for k in kmers:
            print(k)
