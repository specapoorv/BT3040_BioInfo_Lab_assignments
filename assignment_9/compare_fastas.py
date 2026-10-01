import sys


def parse_fasta_headers(filepath):
    ids = set()
    with open(filepath, "r") as f:
        for line in f:
            if line.startswith(">"):
                header_id = line[1:].strip().split()[0] #just take the header_id and store it
                ids.add(header_id)
    return ids


pdbtm_file = "pdbtm_beta_barrel_nr.fasta"  # PDBTM non-redundant set
cdhit_file = "pdbtm_nr40.fasta"  #CD-HIT 40% output set

pdbtm_ids = parse_fasta_headers(pdbtm_file)
cdhit_ids = parse_fasta_headers(cdhit_file)

common = pdbtm_ids & cdhit_ids #python supports these kind of operations between sets
only_pdbtm = pdbtm_ids - cdhit_ids
only_cdhit = cdhit_ids - pdbtm_ids


print(f"Total sequences in PDBTM NR set : {len(pdbtm_ids)}")
print(f"Total sequences in CD-HIT 40%   : {len(cdhit_ids)}")
print(f"Shared in both sets (overlap)   : {len(common)}")
print(f"Unique to PDBTM NR              : {len(only_pdbtm)}")
print(f"Unique to CD-HIT 40%            : {len(only_cdhit)}")

if len(pdbtm_ids | cdhit_ids) > 0:
    jaccard = len(common) / len(pdbtm_ids | cdhit_ids) * 100
    print(f"Jaccard similarity              : {jaccard:.2f}%")

# Save overlapping and unique IDs to text files
with open("shared_ids.txt", "w") as f:
    f.writelines(f"{seq_id}\n" for seq_id in sorted(common))

with open("only_pdbtm_ids.txt", "w") as f:
    f.writelines(f"{seq_id}\n" for seq_id in sorted(only_pdbtm))

with open("only_cdhit_ids.txt", "w") as f:
    f.writelines(f"{seq_id}\n" for seq_id in sorted(only_cdhit))

