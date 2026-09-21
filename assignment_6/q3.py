import sys


#gemini made this helper to parse the file
def parse_al2co_file(filepath):
    data = []
    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("*") or line.startswith("al2co"):
                continue

            parts = line.split()
            if len(parts) >= 3 and parts[0].isdigit():
                pos = int(parts[0])
                res = parts[1]
                if "*" in parts or parts[2].endswith("*"):
                    continue

                score_str = parts[2].replace("*", "")
                try:
                    score = float(score_str)
                    data.append((pos, res, score))
                except ValueError:
                    continue
    return data

# i wrote this
def print_top_conservation(data, n=10):
    sorted_highest = sorted(data, key=lambda x: x[2], reverse=True)[:n]
    sorted_lowest = sorted(data, key=lambda x: x[2])[:n]

    print(f"Top {n} Highest Conservation Scores")
    print(f"{'Rank':<6}{'Position':<10}{'Residue':<10}{'Score':<10}")
    for rank, (pos, res, score) in enumerate(sorted_highest, start=1):
        print(f"{rank:<6}{pos:<10}{res:<10}{score:<10.3f}")

    print(f"Top {n} Lowest Conservation Scores")
    print(f"{'Rank':<6}{'Position':<10}{'Residue':<10}{'Score':<10}")
    for rank, (pos, res, score) in enumerate(sorted_lowest, start=1):
        print(f"{rank:<6}{pos:<10}{res:<10}{score:<10.3f}")

if __name__ == "__main__":
    filename = (
        sys.argv[1]
        if len(sys.argv) > 1
        else "/home/specapoorv/bioinfo/assignment_6/set1_method1_entropy_unweighted.txt"
    )
    records = parse_al2co_file(filename)
    print_top_conservation(records, n=10)