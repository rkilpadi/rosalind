# scans a .txt file containing a single line of nucleotides
# returns a stripped string
def scan_gene(filename):
    with open(filename, "r") as data:
        return data.read().rstrip()