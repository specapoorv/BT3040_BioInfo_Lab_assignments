s1 = "MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH"
s2 = "MVHWTAEEKQLITGLWGKVNVAECGAEALARLLIVYPWTQRFFASFGNLSSPTAILGNPMVRAHGKKVLTSFGDAVKNLDNIKNTFSQLSELHCDKLHVDPENFRLLGDILIIVLAAHFSKDFTPECQAAWQKLVRVVAHALARKYH"

similar_groups = [
    ["K", "R", "H"],
    ["D", "E"],
    ["I", "L", "V", "M"],
    ["F", "Y", "W"],
    ["S", "T"],
    ["A", "G"]
]

matches = 0
similars = 0
gaps = 0
total_len = len(s1)

for i in range(total_len):
    c1 = s1[i]
    c2 = s2[i]
    
    if c1 == "-" or c2 == "-":
        gaps = gaps + 1
    elif c1 == c2:
        matches = matches + 1
        similars = similars + 1
    else:
        for g in similar_groups:
            if c1 in g and c2 in g:
                similars = similars + 1
                break

orig_query_len = 147
query_aligned_bases = 0
for ch in s1:
    if ch != "-":
        query_aligned_bases = query_aligned_bases + 1

ident_pct = (matches / total_len) * 100
sim_pct = (similars / total_len) * 100
gap_pct = (gaps / total_len) * 100
cov_pct = (query_aligned_bases / orig_query_len) * 100

print("Length:", total_len)
print("Matches:", matches)
print("Similars:", similars)
print("Gaps:", gaps)
print("Identity %:", ident_pct)
print("Similarity %:", sim_pct)
print("Gap %:", gap_pct)
print("Query Coverage %:", cov_pct)