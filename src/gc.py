from Bio import SeqIO


# Return: The ID of the string having the highest GC-content,
# followed by the GC-content of that string
def compute_highest_gc(filename):
    largest = ('', 0)  # seq, gc_content
    for record in SeqIO.parse(filename, 'fasta'):
        gc_count = 0
        for char in record.seq:
            if char == 'G' or char == 'C':
                gc_count += 1
        gc_content = 100 * gc_count / len(record.seq)
        if gc_content > largest[1]:
            largest = (record.id, gc_content)
    return largest


if __name__ == "__main__":
    result = compute_highest_gc('data/rosalind_gc.txt')
