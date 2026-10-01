import sys


def compare_files(file1, file2):
    with open(file1, "r") as f1, open(file2, "r") as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    if lines1 == lines2:
        print("MATCH: Both files are completely identical.")
        return True

    print("MISMATCH: The files differ.\n")
    max_len = max(len(lines1), len(lines2))

    diff_count = 0
    for idx in range(max_len):
        l1 = lines1[idx] if idx < len(lines1) else "<EOF>"
        l2 = lines2[idx] if idx < len(lines2) else "<EOF>"

        if l1 != l2:
            diff_count += 1
            print(f"--- Line {idx + 1} difference ---")
            print(f"File 1: {repr(l1)}")
            print(f"File 2: {repr(l2)}")
            if diff_count >= 10:
                print(
                    "\n...more differences found. Showing first 10 differences"
                    " only."
                )
                break

    return False


if __name__ == "__main__":
    if len(sys.argv) < 3:
        f1 = "pattern_a_matches.txt"
        f2 = "online_pattern_a_matches.txt"
    else:
        f1 = sys.argv[1]
        f2 = sys.argv[2]

    compare_files(f1, f2)