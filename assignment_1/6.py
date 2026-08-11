dna_sequence = "GACATTGTGAACAGTAAAAAAGTCCATGCAATGCGCAAGGAGCAGAAGAGGAAGCAGGGCAAGCAGCGCTCCATGGGCTCTCCCATGGACTACTCTCCTCTGCCCATCGACAAGCATGAGCCTGAATTTGGTCCATGCAGAAGAAAACTGGATGGG"
search_strings = ['AAG', 'GTC', 'GAG', 'ACTA', 'ATAT']

for target in search_strings:

    print(f"Enter the string: {target}")
    positions = []
    index = dna_sequence.find(target)
    while index != -1:
        positions.append(str(index + 1))
        index = dna_sequence.find(target, index + 1)
    print(f"Total match: {len(positions)}")
    if positions:
        print(f"Position of match: {', '.join(positions)}")
    else:
        print("Position of match: 0")
