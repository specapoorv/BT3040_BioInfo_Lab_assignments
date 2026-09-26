# table values:
# row 30: Hgm
# row 19: Ca
# row 14: Et

p = {
    "A": {"hgm": 13.85, "ca": 20.0, "et": 1.90},
    "D": {"hgm": 11.61, "ca": 26.0, "et": 1.52},
    "C": {"hgm": 15.37, "ca": 25.0, "et": 2.04},
    "E": {"hgm": 11.38, "ca": 33.0, "et": 1.54},
    "F": {"hgm": 13.93, "ca": 46.0, "et": 1.86},
    "G": {"hgm": 13.34, "ca": 13.0, "et": 1.90},
    "H": {"hgm": 13.82, "ca": 37.0, "et": 1.76},
    "I": {"hgm": 15.28, "ca": 39.0, "et": 1.95},
    "K": {"hgm": 11.58, "ca": 46.0, "et": 1.37},
    "L": {"hgm": 14.13, "ca": 35.0, "et": 1.97},
    "M": {"hgm": 13.86, "ca": 43.0, "et": 1.96},
    "N": {"hgm": 13.02, "ca": 28.0, "et": 1.56},
    "P": {"hgm": 12.35, "ca": 22.0, "et": 1.70},
    "Q": {"hgm": 12.61, "ca": 36.0, "et": 1.52},
    "R": {"hgm": 13.10, "ca": 55.0, "et": 1.48},
    "S": {"hgm": 13.39, "ca": 20.0, "et": 1.75},
    "T": {"hgm": 12.70, "ca": 28.0, "et": 1.77},
    "V": {"hgm": 14.56, "ca": 33.0, "et": 1.98},
    "W": {"hgm": 15.48, "ca": 61.0, "et": 1.87},
    "Y": {"hgm": 13.88, "ca": 46.0, "et": 1.69},
}

s1 = "RATPTRWPVGCFNRPWTKWSYDEALDGIKAAGYAWTGLLTASKPSLHHATATPEYLAALKQKSRHAA"
s2 = "AAAVMMGLAAIGAAIGIGILGGKFLEGAARQPDLIPLLRTQFFIVMGLVDAIPMIAVGLGLYVMFAVA"
s3 = "AADVSAAVGATGQSGMTYRLGLSWDWDKSWWQTSTGRLTGYWDAGYTYWEGGDEGAGKHSLSFAPVFVYEFAGDSIKPFIEAGIGVAAFSGTRVGDQNLGSSLNFEDRIGAGLKFANGQSVGVRAIHYSNAGLKQPNDGIESYSLFYKIPI"

for i, s in enumerate([s1, s2, s3], 1):
    n = len(s)
    tot_h = sum(p[x]["hgm"] for x in s)
    tot_ca = sum(p[x]["ca"] for x in s)
    tot_et = sum(p[x]["et"] for x in s)
    print(
        f"seq{i}: hgm={tot_h/n:.3f}, ca={tot_ca/n:.2f}, et={tot_et/n:.2f} (len={n})"
    )