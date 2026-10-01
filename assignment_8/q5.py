import re

# pattern: [SV]-T-[VT]-[DERK](2)-{IL}
pat_a = re.compile(r"[SV]T[VT][DERK]{2}[^IL]")


def read_fasta(filename):
    hdr = None
    seq_parts = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if hdr:
                    yield hdr, "".join(seq_parts)
                hdr = line[1:]
                seq_parts = []
            else:
                seq_parts.append(line)
        if hdr:
            yield hdr, "".join(seq_parts)


in_file = "Q4.fasta"
out_file = "pattern_a_matches.txt"

with open(out_file, "w") as out:
    out.write(">USER001 (user pattern):\n")
    out.write("Pattern: [SV]-T-[VT]-[DERK](2)-{IL}\n")
\
    for header, seq in read_fasta(in_file):
        matches = []
        for m in re.finditer(r"(?=(" + pat_a.pattern + r"))", seq):
            start = m.start() + 1
            hit = m.group(1)
            end = start + len(hit) - 1
            matches.append((start, end, hit))

        if matches:
            hdr_display = header.split(",")[0].split()[0]
            out.write(f">{hdr_display}\n")
            for s, e, hit in matches:
                out.write(f"      {s} - {e}:        {hit}\n")
            out.write("\n\n")

print(f"Results written to {out_file}")