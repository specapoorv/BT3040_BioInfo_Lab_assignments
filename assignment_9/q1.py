import math

# Input sequences
seq1 = "AMENLNMDLLYMAAAVMMGLAAIGAAIGIGILGGKFLEGAARQPDLIPLLRTQFFIVMGLVDAIPMIAVGLGLYVMFAVA"
seq2 = "AADVSAAVGATGQSGMTYRLGLSWDWDKSWWQTSTGRLTGYWDAGYTYWEGGDEGAGKHSLSFAPVFVYEFAGDSIKPFIEAGIGVAAFSGTRVGDQNLGSSLNFEDRIGAGLKFANGQSVGVRAIHYSNAGLKQPNDGIESYSLFYKIPI"
seq3 = "MALLPAAPGAPARATPTRWPVGCFNRPWTKWSYDEALDGIKAAGYAWTGLLTASKPSLHHATATPEYLAALKQKSRHAA"

print(f"Length of Sequence 1: {len(seq1)}")
print(f"Length of Sequence 2: {len(seq2)}")
print(f"Length of Sequence 3: {len(seq3)}")


 #Hamming Distance (requires equal lengths)
def hamming_distance(s1, s2):
    if len(s1) != len(s2):
        return None  #cannot compare equal lengths

    mismatches = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            mismatches += 1
    return mismatches


print("HAMMING DISTANCE:")
pairs = [("Seq 1 and Seq 2", seq1, seq2),
         ("Seq 1 and Seq 3", seq1, seq3),
         ("Seq 2 and Seq 3", seq2, seq3)]

for name, s1, s2 in pairs:
    dist = hamming_distance(s1, s2)
    if dist is None:
        print(f"{name}: Undefined (different lengths)")
    else:
        norm_dist = dist / len(s1)
        print(f"{name}: {dist} mismatches (normalized: {norm_dist:.4f})")



#Euclidean Distance (using Amino Acid Frequencies)
amino_acids = "ACDEFGHIKLMNPQRSTVWY"

def get_frequencies(seq):
    freq = {}
    for aa in amino_acids:
        freq[aa] = 0.0

    for aa in seq:
        if aa in freq:
            freq[aa] += 1

    total_len = len(seq)
    for aa in freq:
        freq[aa] = freq[aa] / total_len

    return freq

f1 = get_frequencies(seq1)
f2 = get_frequencies(seq2)
f3 = get_frequencies(seq3)

def euclidean_distance(freq_a, freq_b):
    sum_sq = 0.0
    for aa in amino_acids:
        diff = freq_a[aa] - freq_b[aa]
        sum_sq += diff * diff
    return math.sqrt(sum_sq)

d12 = euclidean_distance(f1, f2)
d13 = euclidean_distance(f1, f3)
d23 = euclidean_distance(f2, f3)

print("EUCLIDEAN DISTANCE (Frequency Vectors):")
print(f"Seq 1 and Seq 2: {d12:.4f}")
print(f"Seq 1 and Seq 3: {d13:.4f}")
print(f"Seq 2 and Seq 3: {d23:.4f}")