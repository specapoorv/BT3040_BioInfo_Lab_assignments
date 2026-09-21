import sys
#imported from q3
from q3 import parse_al2co_file


def compare_alignments(f_clustal, f_mafft, f_muscle, threshold=0.1):
    #we have to do this because parse_al2co gives a list of tuples which we will convert into a dict of this manner pos : (res, score)
    c_data = {pos: (res, score) for pos, res, score in parse_al2co_file(f_clustal)}
    m_data = {pos: (res, score) for pos, res, score in parse_al2co_file(f_mafft)}
    u_data = {pos: (res, score) for pos, res, score in parse_al2co_file(f_muscle)}


    common_positions = sorted(set(c_data.keys()) & set(m_data.keys()) & set(u_data.keys()))

    similar = []
    different = []

    for pos in common_positions:
        res = c_data[pos][0]
        s_c = c_data[pos][1]
        s_m = m_data[pos][1]
        s_u = u_data[pos][1]

        diff = max(s_c, s_m, s_u) - min(s_c, s_m, s_u)
        entry = (pos, res, s_c, s_m, s_u, diff)

        if diff <= threshold:
            similar.append(entry)
        else:
            different.append(entry)

    sorted_similar = sorted(similar, key=lambda x: x[5])[:10]

    print(f"=== (i) Top Residues with SIMILAR Conservation Scores (Diff <= {threshold}) ===")
    print(f"{'Pos':<6}{'Res':<6}{'Clustal':<10}{'MAFFT':<10}{'MUSCLE':<10}{'Diff':<10}")
    for item in sorted_similar:
        print(f"{item[0]:<6}{item[1]:<6}{item[2]:<10.3f}{item[3]:<10.3f}{item[4]:<10.3f}{item[5]:<10.3f}")

    #(ii) Different scores (largest differences first)
    sorted_different = sorted(different, key=lambda x: x[5], reverse=True)[:10]

    print(f"\n=== (ii) Top Residues with DIFFERENT Conservation Scores (Diff > {threshold}) ===")
    print(f"{'Pos':<6}{'Res':<6}{'Clustal':<10}{'MAFFT':<10}{'MUSCLE':<10}{'Diff':<10}")
    for item in sorted_different:
        print(f"{item[0]:<6}{item[1]:<6}{item[2]:<10.3f}{item[3]:<10.3f}{item[4]:<10.3f}{item[5]:<10.3f}")

if __name__ == "__main__":
    f_clustal = sys.argv[1] if len(sys.argv) > 1 else "assignment_6/results/set2_method1_entropy_unweighted.txt"
    f_mafft   = sys.argv[2] if len(sys.argv) > 2 else "assignment_6/set2_mafft_entropy.txt"
    f_muscle  = sys.argv[3] if len(sys.argv) > 3 else "assignment_6/set2_muscle_entropy.txt"

    compare_alignments(f_clustal, f_mafft, f_muscle)