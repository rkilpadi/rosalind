# Return: The total number of rabbit pairs that will be present after n months,
# if we begin with 1 pair and in each generation,
# every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
def breed_rabbits(months, litter_size):
    adults, babies = 1, litter_size
    for i in range(months - 2):
        newborns = adults * litter_size
        adults += babies
        babies = newborns
    return adults


if __name__ == "__main__":
    with open('data/rosalind_fib.txt', 'r') as data:
        nums = data.readline().split(' ')
        print(breed_rabbits(int(nums[0]), int(nums[1])))
