# Return: The total number of rabbit pairs that will be present after n months,
# if we begin with 1 pair and in each generation,
# every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
def breed_rabbits(filename):
    with open(filename, 'r') as data:
        nums = data.readline().split(' ')
        months, litter_size = int(nums[0]), int(nums[1])

    adults, babies = 1, litter_size
    for i in range(months - 2):
        newborns = adults * litter_size
        adults += babies
        babies = newborns
    print(adults)


breed_rabbits('data/rosalind_fib.txt')
