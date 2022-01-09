# Returns the Hamming distance between two strings
# Hamming distance is the number of mismatched chars
def hamming_distance(str1, str2):
    distance = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1
    return distance


if __name__ == "__main__":
    with open('../data/rosalind_hamm.txt', 'r') as data:
        genes = data.readlines()
        print(hamming_distance(genes[0], genes[1]))
