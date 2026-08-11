
dna_sequence = "CTCGGATTTGTAAAGATCATGATCTCATACATAGTACCTAGCCA"

energy_matrix = {
    'AA': -4, 'AT': -7, 'AC': -5, 'AG': -11, 
    'TA': -7, 'TT': -2, 'TC': -3, 'TG': -4, 
    'CA': -9, 'CT': -5, 'CC': -6, 'CG': -7, 
    'GA': -9, 'GT': -6, 'GC': -4, 'GG': -11
}

total_energy = 0
num_pairs = len(dna_sequence) - 1

for i in range(num_pairs):
    dinucleotide = dna_sequence[i:i+2]
    total_energy += energy_matrix[dinucleotide]

average_energy = total_energy / num_pairs

print(f"Sequence: {dna_sequence}")
print(f"Total base stacking energy: {total_energy}")
print(f"Average base stacking energy: {average_energy:.4f}")