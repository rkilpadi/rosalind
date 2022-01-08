# Return: The total number of pairs of rabbits that will remain
# after the n-th month if all rabbits live for m months
def breed_rabbits(n, m):
    rabbits = [1, 1, 1]
    for months in range(n-2):
        if months < m - 1:
            rabbits.append(rabbits[-1] + rabbits[-2])
        else:
            rabbits.append(rabbits[-1] + rabbits[-2] - rabbits.pop(0))
    return rabbits[-1]


if __name__ == "__main__":
    with open('data/rosalind_fibd.txt', 'r') as data:
        nums = data.readline().split(' ')
        print(breed_rabbits(int(nums[0]), int(nums[1])))
