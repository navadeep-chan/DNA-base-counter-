from Bio import SeqIO
from Bio.SeqUtils import gc_fraction


def parse_fasta(file_path: str):
    for record in SeqIO.parse(file_path, "fasta"):
        seq_id = record.id
        length = len(record.seq)
        gc_pct = gc_fraction(record.seq) * 100

        print(f"ID: {seq_id:<15} Length: {length:<8} GC Content: {gc_pct:.2f}%")

sequence = input("Please enter your fasta file name (with extension): ")
parse_fasta(sequence)