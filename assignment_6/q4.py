import math
AMINO_ACIDS = list("ACDEFGHIKLMNPQRSTVWY")

'''
# load blosum62 function is written by gemini, basically takes the BLOSUM62 txt files and just gives the matrix
   A  R  N  D  C  Q  E  G  H  I  L  K  M  F  P  S  T  W  Y  V  B  Z  X  *
A  4 -1 -2 -2  0 -1 -1  0 -2 -1 -1 -1 -1 -2 -1  1  0 -3 -2  0 -2 -1  0 -4 
R -1  5  0 -2 -3  1  0 -2  0 -3 -2  2 -1 -3 -2 -1 -1 -3 -2 -3 -1  0 -1 -4 
N -2  0  6  1 -3  0  0  0  1 -3 -3  0 -2 -3 -2  1  0 -4 -2 -3  3  0 -1 -4 
D -2 -2  1  6 -3  0  2 -1 -1 -3 -4 -1 -3 -3 -1  0 -1 -4 -3 -3  4  1 -1 -4 
C  0 -3 -3 -3  9 -3 -4 -3 -3 -1 -1 -3 -1 -2 -3 -1 -1 -2 -2 -1 -3 -3 -2 -4 
Q -1  1  0  0 -3  5  2 -2  0 -3 -2  1  0 -3 -1  0 -1 -2 -1 -2  0  3 -1 -4 
E -1  0  0  2 -4  2  5 -2  0 -3 -3  1 -2 -3 -1  0 -1 -3 -2 -2  1  4 -1 -4 
G  0 -2  0 -1 -3 -2 -2  6 -2 -4 -4 -2 -3 -3 -2  0 -2 -2 -3 -3 -1 -2 -1 -4 
H -2  0  1 -1 -3  0  0 -2  8 -3 -3 -1 -2 -1 -2 -1 -2 -2  2 -3  0  0 -1 -4 
I -1 -3 -3 -3 -1 -3 -3 -4 -3  4  2 -3  1  0 -3 -2 -1 -3 -1  3 -3 -3 -1 -4 
L -1 -2 -3 -4 -1 -2 -3 -4 -3  2  4 -2  2  0 -3 -2 -1 -2 -1  1 -4 -3 -1 -4 
K -1  2  0 -1 -3  1  1 -2 -1 -3 -2  5 -1 -3 -1  0 -1 -3 -2 -2  0  1 -1 -4 
M -1 -1 -2 -3 -1  0 -2 -3 -2  1  2 -1  5  0 -2 -1 -1 -1 -1  1 -3 -1 -1 -4 
F -2 -3 -3 -3 -2 -3 -3 -3 -1  0  0 -3  0  6 -4 -2 -2  1  3 -1 -3 -3 -1 -4 
P -1 -2 -2 -1 -3 -1 -1 -2 -2 -3 -3 -1 -2 -4  7 -1 -1 -4 -3 -2 -2 -1 -2 -4 
S  1 -1  1  0 -1  0  0  0 -1 -2 -2  0 -1 -2 -1  4  1 -3 -2 -2  0  0  0 -4 
T  0 -1  0 -1 -1 -1 -1 -2 -2 -1 -1 -1 -1 -2 -1  1  5 -2 -2  0 -1 -1  0 -4 
W -3 -3 -4 -4 -2 -2 -3 -2 -2 -3 -2 -3 -1  1 -4 -3 -2 11  2 -3 -4 -3 -2 -4 
Y -2 -2 -2 -3 -2 -1 -2 -3  2 -1 -1 -2 -1  3 -3 -2 -2  2  7 -1 -3 -2 -1 -4 
V  0 -3 -3 -3 -1 -2 -2 -3 -3  3  1 -2  1 -1 -2 -2  0 -3 -1  4 -3 -2 -1 -4 
B -2 -1  3  4 -3  0  1 -1  0 -3 -4  0 -3 -3 -2  0 -1 -4 -3 -3  4  1 -1 -4 
Z -1  0  0  1 -3  3  4 -2  0 -3 -3  1 -1 -3 -1  0 -1 -3 -2 -2  1  4 -1 -4 
X  0 -1 -1 -1 -2 -1 -1 -1 -1 -1 -1 -1 -1 -1 -2  0  0 -2 -1 -1 -1 -1 -1 -4 
* -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4  1 
'''
def load_blosum62(matrix_file="BLOSUM62"):
    matrix = {}
    with open(matrix_file) as f:
        headers = []
        for line in f:
            if line.startswith("#") or not line.strip():
                continue
            parts = line.split()
            if not headers:
                headers = parts
            else:
                aa = parts[0]
                scores = [int(x) for x in parts[1:]]
                for other_aa, score in zip(headers, scores):
                    matrix[(aa, other_aa)] = score
    return matrix


def read_clustal(filename):
    sequences = {}
    with open(filename) as f:
        for line in f:
            line = line.strip()
            #skip header
            if not line or line.startswith("CLUSTAL") or line[0] in "*:. ":
                continue
            parts = line.split()
            if len(parts) >= 2:
                seq_id, seq = parts[0], parts[1]
                if seq_id not in sequences:
                    sequences[seq_id] = ""
                sequences[seq_id] += seq
    return list(sequences.values())


def calc_entropy(freqs):
    #C(i) = sum( f_a * ln(f_a) )
    score = 0.0
    for aa in AMINO_ACIDS:
        f = freqs[aa]
        if f > 0:
            score += f * math.log(f)
    return score


def calc_variance(freqs, bg_freq=1.0 / 20.0):
    # C(i) = sqrt( sum( (f_a - f_overall)^2 ) )
    sq_diff_sum = sum((freqs[aa] - bg_freq) ** 2 for aa in AMINO_ACIDS)
    return math.sqrt(sq_diff_sum)


def calc_sum_of_pairs(freqs, matrix):
    # C(i) = sum_a sum_b ( f_a * f_b * S_ab )
    score = 0.0
    for a in AMINO_ACIDS:
        for b in AMINO_ACIDS:
            if freqs[a] > 0 and freqs[b] > 0:
                score += freqs[a] * freqs[b] * matrix.get((a, b), 0)
    return score


def main():
    aln_file = "SetA.aln"
    blosum_file = "BLOSUM62"

    seqs = read_clustal(aln_file)
    matrix = load_blosum62(blosum_file)

    num_seqs = len(seqs)
    aln_len = len(seqs[0])

    print(f"{'Pos':<6}{'Entropy':<12}{'Variance':<12}{'SumOfPairs':<12}")

    for i in range(aln_len):
        col = [s[i].upper() for s in seqs]

        #ignore gaps to count frequencies
        valid_aas = [aa for aa in col if aa in AMINO_ACIDS]

        if not valid_aas:
            continue

        #nweighted frequencies: count / total_valid
        freqs = {aa: valid_aas.count(aa) / len(valid_aas) for aa in AMINO_ACIDS}

        entropy_score = calc_entropy(freqs)
        variance_score = calc_variance(freqs)
        sop_score = calc_sum_of_pairs(freqs, matrix)

        print(
            f"{i+1:<6}{entropy_score:<12.3}{variance_score:<12.3}{sop_score:<12.3}"
        )


if __name__ == "__main__":
    main()