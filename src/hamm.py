# Returns the Hamming distance between two strings
# Hamming distance is the number of mismatched chars
def hamming_distance(filename):
    with open(filename, 'r') as data:
        genes = data.readlines()

    distance = 0
    for i in range(len(genes[0])):
        if genes[0][i] != genes[1][i]:
            distance += 1
    print(distance)


hamming_distance('data/rosalind_hamm.txt')
