# Given: A positive integer n (n≤20,000) and two subsets A and B of {1,2,…,n}.
# Return: Six sets: A∪B, A∩B, A−B, B−A, Ac, and Bc (where set complements are taken with respect to {1,2,…,n}).
def set_to_string(s):
    return '{' + ', '.join(map(str, s)) + '}'


with open('../data/rosalind_seto.txt') as input_data:
    lines = input_data.readlines()
    # Convert to sets.
    superset = set([i for i in range(1, int(lines[0]) + 1)])
    A = set(map(int, lines[1].rstrip().rstrip('}').lstrip('{').split(', ')))
    B = set(map(int, lines[2].rstrip().rstrip('}').lstrip('{').split(', ')))
    f = open('../results/seto_results.txt', 'w')
    f.write(set_to_string(A | B) + '\n')
    f.write(set_to_string(A & B) + '\n')
    f.write(set_to_string(A - B) + '\n')
    f.write(set_to_string(B - A) + '\n')
    f.write(set_to_string(superset - A) + '\n')
    f.write(set_to_string(superset - B) + '\n')
    f.close()
