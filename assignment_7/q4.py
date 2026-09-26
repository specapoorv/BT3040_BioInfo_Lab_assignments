aa = "ACDEFGHIKLMNPQRSTVWY"

s1 = "RATPTRWPVGCFNRPWTKWSYDEALDGIKAAGYAWTGLLTASKPSLHHATATPEYLAALKQKSRHAA"
s2 = "AAAVMMGLAAIGAAIGIGILGGKFLEGAARQPDLIPLLRTQFFIVMGLVDAIPMIAVGLGLYVMFAVA"
s3 = "AADVSAAVGATGQSGMTYRLGLSWDWDKSWWQTSTGRLTGYWDAGYTYWEGGDEGAGKHSLSFAPVFVYEFAGDSIKPFIEAGIGVAAFSGTRVGDQNLGSSLNFEDRIGAGLKFANGQSVGVRAIHYSNAGLKQPNDGIESYSLFYKIPI"

for sn, s in [("seq1", s1), ("seq2", s2), ("seq3", s3)]:
    print("=" * 40)
    print(sn)
    n = len(s)
    f = {x: s.count(x) for x in aa}
    nij = {}
    for a1 in aa:
        for a2 in aa:
            nij[(a1, a2)] = 0
    for i in range(n - 1):
        p = (s[i], s[i + 1])
        nij[p] += 1

    pa = {}
    pb = {}
    pc = {}

    for a1 in aa:
        for a2 in aa:
            cnt = nij[(a1, a2)]
            # (a) Nij * 100 / (Ni + Nj)
            if f[a1] + f[a2] > 0:
                pa[(a1, a2)] = (cnt * 100.0) / (f[a1] + f[a2])
            else:
                pa[(a1, a2)] = 0.0

            # (b) Nij * 100 / (N - 1)
            pb[(a1, a2)] = (cnt * 100.0) / (n - 1)

            # (c) Nij * 100 / (Ni * Nj)
            if f[a1] * f[a2] > 0:
                pc[(a1, a2)] = (cnt * 100.0) / (f[a1] * f[a2])
            else:
                pc[(a1, a2)] = 0.0

    print("--- 20x20 table pref (b) ---")
    print("  " + " ".join([f"{x:>5}" for x in aa]))
    for a1 in aa:
        row = [f"{pb[(a1, a2)]:5.2f}" for a2 in aa]
        print(f"{a1} " + " ".join(row))

    print("\ntop 10 pref (a):")
    t1 = sorted(pa.items(), key=lambda z: z[1], reverse=True)[:10]
    for k, v in t1:
        print(f"{k[0]}{k[1]}: {v:.2f}")

    print("\ntop 10 pref (b):")
    t2 = sorted(pb.items(), key=lambda z: z[1], reverse=True)[:10]
    for k, v in t2:
        print(f"{k[0]}{k[1]}: {v:.2f}")

    print("\ntop 10 pref (c):")
    t3 = sorted(pc.items(), key=lambda z: z[1], reverse=True)[:10]
    for k, v in t3:
        print(f"{k[0]}{k[1]}: {v:.2f}")