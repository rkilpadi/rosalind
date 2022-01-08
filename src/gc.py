from Bio import SeqIO


# Return: The ID of the string having the highest GC-content,
# followed by the GC-content of that string
def compute_gc(filename):
    largest = ('', 0)  # seq, gc_content
    for record in SeqIO.parse(filename, 'fasta'):
        gc_count = 0
        for char in record.seq:
            if char == 'G' or char == 'C':
                gc_count += 1
        gc_content = 100 * gc_count / len(record.seq)
        if gc_content > largest[1]:
            largest = (record.id, gc_content)
    print(largest[0])
    print(largest[1])


compute_gc('data/rosalind_gc.txt')
