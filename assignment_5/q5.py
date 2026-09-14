s1 = "MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH"
s2 = "MVHWTAEEKQLITGLWGKVNVAECGAEALARLLIVYPWTQRFFASFGNLSSPTAILGNPMVRAHGKKVLTSFGDAVKNLDNIKNTFAQLSELHCDKLHVDPENFRLLGDILIIVLAAHFSKDFTPECQAAWQKLVRVVAHALAHKYH"

d1 = {}
d2 = {}

for i in range(len(s1) - 4):
    p = s1[i:i+5]
    if p in d1:
        d1[p] = d1[p] + 1
    else:
        d1[p] = 1

for i in range(len(s2) - 4):
    p = s2[i:i+5]
    if p in d2:
        d2[p] = d2[p] + 1
    else:
        d2[p] = 1

ans = []
for k in d1:
    if k in d2:
        ans.append(k)

print("Matching pentapeptides:", len(ans))
print("peptide seq1_count seq2_count")

for x in ans:
    print(x, "\t", d1[x], "\t", d2[x])