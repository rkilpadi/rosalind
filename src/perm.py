from itertools import permutations  # cheating :P


# Return: The total number of permutations of length n
# followed by a list of all such permutations
def permute(n):
    return permutations(list(range(1, n+1)))


if __name__ == "__main__":
    with open('../data/rosalind_perm.txt', 'r') as data:
        perms = list(permute(int(data.read())))
        print(len(perms))
        for perm in perms:
            to_print = ''
            for num in perm:
                to_print += str(num) + ' '
            print(to_print)
