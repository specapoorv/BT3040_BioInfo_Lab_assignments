# BT3040 - Assignment 6: Positional Conservation Analysis

This repository contains the dataset, scripts, alignment files, and output results for **Assignment 6 (BT3040: Introduction to Bioinformatics)**.

- **Base URL:** [https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6)
- **Questionnaire:** [BT3040_Assignment_6.pdf](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/BT3040_Assignment_6.pdf)
- **Report & Solutions:** [Solution 6.pdf](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/Solution%206.pdf)

---

## Quick Summary of Questions & Files

### Q1 & Q2: AL2CO Conservation Scores (CLI & Web Server)
- **Input Sequences (Set 1 - Globins)**: [SetA.fasta](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/SetA.fasta)
- **Input Sequences (Set 2 - TIM)**: [SetB.fasta](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/SetB.fasta)
- **Clustal Omega MSA (Set 1)**: [SetA.aln](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/SetA.aln)
- **Clustal Omega MSA (Set 2)**: [SetB.aln](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/SetB.aln)
- **Scoring Matrix**: [BLOSUM62](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/BLOSUM62)
- **AL2CO Tool Source & Binary**: [al2co/](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/al2co)
- **Results for Set 1 (Globins)**:
  - Result #1 (Method i - Unweighted Entropy): [results/set1_method1_entropy_unweighted.txt](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/results/set1_method1_entropy_unweighted.txt)
  - Result #2 (Method ii - Unweighted Variance): [results/set1_method2_variance_unweighted.txt](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/results/set1_method2_variance_unweighted.txt)
  - Result #3 (Method iii - Sum of Pairs with BLOSUM62): [results/set1_method3_sum_of_pairs.txt](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/results/set1_method3_sum_of_pairs.txt)
  - Result #4 (Method iv - Weighted Variance): [results/set1_method4_variance_weighted.txt](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/results/set1_method4_variance_weighted.txt)
  - Result #5 (Method v - Normalized Entropy): [results/set1_method5_entropy_normalized.txt](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/results/set1_method5_entropy_normalized.txt)
- **Results for Set 2 (TIM)**:
  - Result #1 (Method i - Unweighted Entropy): [results/set2_method1_entropy_unweighted.txt](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/results/set2_method1_entropy_unweighted.txt)
  - Result #2 (Method ii - Unweighted Variance): [results/set2_method2_variance_unweighted.txt](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/results/set2_method2_variance_unweighted.txt)
  - Result #3 (Method iii - Sum of Pairs with BLOSUM62): [results/set2_method3_sum_of_pairs.txt](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/results/set2_method3_sum_of_pairs.txt)
  - Result #4 (Method iv - Weighted Variance): [results/set2_method4_variance_weighted.txt](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/results/set2_method4_variance_weighted.txt)
  - Result #5 (Method v - Normalized Entropy): [results/set2_method5_entropy_normalized.txt](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/results/set2_method5_entropy_normalized.txt)

### Q3: Top 10 Highest & Lowest Conserved Residues
- **Parser & Ranking Script**: [q3.py](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/q3.py)
- **Input Data (Method i Scores)**:
  - Set 1: [results/set1_method1_entropy_unweighted.txt](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/results/set1_method1_entropy_unweighted.txt)
  - Set 2: [results/set2_method1_entropy_unweighted.txt](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/results/set2_method1_entropy_unweighted.txt)
- **Reported Tables**: See [Solution 6.pdf](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/Solution%206.pdf) (Pages 13–15).

### Q4: Custom Conservation Score Calculation Script
- **Implementation Script**: [q4.py](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/q4.py)
- **Scoring Matrix Input**: [BLOSUM62](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/BLOSUM62)
- **Alignment Input**: [SetA.aln](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/SetA.aln)

### Q5: Comparison of Clustal Omega, MAFFT, and MUSCLE MSAs
- **Comparison Script**: [q5.py](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/q5.py)
- **Set 1 Alignments & Conservation Scores**:
  - Clustal Omega MSA: [SetA.aln](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/SetA.aln) | Scores: [results/set1_method1_entropy_unweighted.txt](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/results/set1_method1_entropy_unweighted.txt)
  - MAFFT MSA: [SetA-mafft.aln](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/SetA-mafft.aln) | Scores: [set1_mafft_entropy.txt](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/set1_mafft_entropy.txt)
  - MUSCLE MSA: [SetA-Muscle.aln](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/SetA-Muscle.aln) | Scores: [set1_muscle_entropy.txt](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/set1_muscle_entropy.txt)
- **Set 2 Alignments & Conservation Scores**:
  - Clustal Omega MSA: [SetB.aln](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/SetB.aln) | Scores: [results/set2_method1_entropy_unweighted.txt](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/results/set2_method1_entropy_unweighted.txt)
  - MAFFT MSA: [SetB-mafft.aln](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/SetB-mafft.aln) | Scores: [set2_mafft_entropy.txt](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/set2_mafft_entropy.txt)
  - MUSCLE MSA: [SetB-Muscle.aln](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/SetB-Muscle.aln) | Scores: [set2_muscle_entropy.txt](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/set2_muscle_entropy.txt)

### Q6: Manual Calculation & Verification at Positions 9, 11, 20, 22, 30
- **Alignment Input**: [SetA.aln](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/SetA.aln)
- **AL2CO Reference Output**: [results/set1_method1_entropy_unweighted.txt](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/results/set1_method1_entropy_unweighted.txt)
- **Manual Calculations**: Worked out step-by-step in [Solution 6.pdf](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/Solution%206.pdf) (Pages 21–24).

### Q7: ConSurf Analysis of 1BTM (Chain A)
- **ConSurf Homolog MSA**: [1BTM.aln](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/1BTM.aln)
- **ConSurf Output Grades**: [1BTM_A_consurf_grades.txt](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/1BTM_A_consurf_grades.txt)

---

## Detailed Question-by-Question Guide

### Questions 1 & 2: Positional Conservation Scores using AL2CO
1. **Set 1**: 11 Alpha-globin sequences (`P69905`, `P01946`, `P01942`, `P01966`, `P01958`, `P01959`, `P01965`, `P06635`, `P60529`, `P80043`, `P01980`).
2. **Set 2**: 9 Triosephosphate isomerase (TIM) sequences (`TPIS_HUMAN`, `TPIS_YEAST`, `TPIS_GRAGA`, `TPIS_TRYCR`, `TPIS_MAIZE`, `TPIS_MOUSE`, `TPIS_DROME`, `TPIS_RABIT`, `TPIS_CAEEL`).
3. Conservation scores were computed across 5 methods:
   - **Method (i)**: Unweighted frequency and entropy-based measure: $C(i) = \sum_a f_a \ln(f_a)$
   - **Method (ii)**: Unweighted frequency and variance-based measure: $C(i) = \sqrt{\sum_a (f_a - f_{overall})^2}$
   - **Method (iii)**: Unweighted frequency and sum of pairs measure using `BLOSUM62`: $C(i) = \sum_a \sum_b f_a f_b S_{ab}$
   - **Method (iv)**: Weighted frequency and variance-based measure (using Henikoff / sequence weights)
   - **Method (v)**: Normalized entropy scores (mean 0, variance 1)

All output files are saved in [`results/`](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/results).

---

### Question 3: Top 10 Residues with Highest and Lowest Conservation
- Script [`q3.py`](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/q3.py) reads the AL2CO entropy output and extracts the 10 most conserved (entropy $= 0.000$) and 10 least conserved (most negative entropy) residue positions.
- **Run command**:
  ```bash
  python3 q3.py results/set1_method1_entropy_unweighted.txt
  python3 q3.py results/set2_method1_entropy_unweighted.txt
  ```

---

### Question 4: Python Implementation of Conservation Measures
- Script [`q4.py`](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/q4.py) computes:
  - Unweighted amino acid frequencies (ignoring gap characters).
  - Shannon entropy score.
  - Variance-based score ($f_{overall} = 1/20 = 0.05$).
  - Sum of pairs score using the BLOSUM62 substitution matrix.
- **Run command**:
  ```bash
  python3 q4.py
  ```

---

### Question 5: Comparison of Clustal Omega, MAFFT, and MUSCLE
- Script [`q5.py`](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/q5.py) aligns and compares positions among the three alignment tools:
  - **Set 1**: All 3 aligners yield identical alignments (difference $= 0.000$) due to very high sequence similarity among globin chains.
  - **Set 2**: Highly conserved catalytic core matches completely, while divergent loop regions (e.g., positions 71 and 126) show differences in gap placements by MUSCLE compared to Clustal Omega and MAFFT.
- **Run command**:
  ```bash
  python3 q5.py results/set2_method1_entropy_unweighted.txt set2_mafft_entropy.txt set2_muscle_entropy.txt
  ```

---

### Question 6: Manual Calculations for Positions 9, 11, 20, 22, 30
Manual verification using the Clustal Omega MSA for Set 1 ([`SetA.aln`](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/SetA.aln)):

| Position | Residue Counts (Total = 11) | Frequency ($f_a$) | $f_a \ln(f_a)$ Contributions | Manual Score | AL2CO Score |
| :---: | :--- | :--- | :--- | :---: | :---: |
| **9** | 2 A, 2 S, 6 T, 1 G | $f_A \approx 0.1818, f_S \approx 0.1818, f_T \approx 0.5455, f_G \approx 0.0909$ | $-0.3099 - 0.3099 - 0.3306 - 0.2180$ | **-1.169** | **-1.169** |
| **11** | 8 V, 3 I | $f_V \approx 0.7273, f_I \approx 0.2727$ | $-0.2316 - 0.3543$ | **-0.586** | **-0.586** |
| **20** | 1 K, 1 S, 7 G, 2 A | $f_K \approx 0.0909, f_S \approx 0.0909, f_G \approx 0.6364, f_A \approx 0.1818$ | $-0.2180 - 0.2180 - 0.2876 - 0.3099$ | **-1.034** | **-1.034** |
| **22** | 9 A, 2 G | $f_A \approx 0.8182, f_G \approx 0.1818$ | $-0.1642 - 0.3099$ | **-0.474** | **-0.474** |
| **30** | 11 L | $f_L = 1.0$ | $1.0 \times \ln(1.0) = 0$ | **0.000** | **0.000** |

---

### Question 7: ConSurf Evolutionary Conservation Analysis (1BTM Chain A)
- Analyzed the crystal structure of 1BTM (Chain A) on the ConSurf web server.
- The homologous alignment was retrieved as [`1BTM.aln`](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/1BTM.aln) and conservation scores / grades (scale 1 to 9) were downloaded as [`1BTM_A_consurf_grades.txt`](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/1BTM_A_consurf_grades.txt).

---

## Master Table of All Files

| File / Directory | Description | Associated Question | GitHub Link |
| :--- | :--- | :---: | :--- |
| **BT3040_Assignment_6.pdf** | Assignment prompt and instructions | All | [BT3040_Assignment_6.pdf](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/BT3040_Assignment_6.pdf) |
| **Solution 6.pdf** | Assignment report & manual calculations | All | [Solution 6.pdf](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/Solution%206.pdf) |
| **BLOSUM62** | BLOSUM62 scoring matrix | Q1, Q2, Q4 | [BLOSUM62](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/BLOSUM62) |
| **al2co/** | AL2CO program source code and compiled binary | Q1, Q2 | [al2co](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/al2co) |
| **SetA.fasta** | Unaligned FASTA sequences for Set 1 (Globins) | Q1, Q2 | [SetA.fasta](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/SetA.fasta) |
| **SetB.fasta** | Unaligned FASTA sequences for Set 2 (TIM) | Q1, Q2 | [SetB.fasta](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/SetB.fasta) |
| **SetA.aln** | Clustal Omega MSA for Set 1 | Q1, Q4, Q5, Q6 | [SetA.aln](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/SetA.aln) |
| **SetB.aln** | Clustal Omega MSA for Set 2 | Q1, Q5 | [SetB.aln](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/SetB.aln) |
| **SetA-mafft.aln** | MAFFT MSA for Set 1 | Q5 | [SetA-mafft.aln](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/SetA-mafft.aln) |
| **SetA-Muscle.aln** | MUSCLE MSA for Set 1 | Q5 | [SetA-Muscle.aln](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/SetA-Muscle.aln) |
| **SetB-mafft.aln** | MAFFT MSA for Set 2 | Q5 | [SetB-mafft.aln](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/SetB-mafft.aln) |
| **SetB-Muscle.aln** | MUSCLE MSA for Set 2 | Q5 | [SetB-Muscle.aln](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/SetB-Muscle.aln) |
| **q3.py** | Python script to extract top 10 highest/lowest residues | Q3 | [q3.py](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/q3.py) |
| **q4.py** | Python implementation of entropy, variance, sum-of-pairs | Q4 | [q4.py](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/q4.py) |
| **q5.py** | Python script comparing Clustal Omega, MAFFT, and MUSCLE | Q5 | [q5.py](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/q5.py) |
| **results/set1_method1_entropy_unweighted.txt** | AL2CO Set 1: Unweighted entropy | Q1, Q2, Q3, Q5, Q6 | [set1_method1_entropy_unweighted.txt](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/results/set1_method1_entropy_unweighted.txt) |
| **results/set1_method2_variance_unweighted.txt** | AL2CO Set 1: Unweighted variance | Q1, Q2 | [set1_method2_variance_unweighted.txt](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/results/set1_method2_variance_unweighted.txt) |
| **results/set1_method3_sum_of_pairs.txt** | AL2CO Set 1: Unweighted sum-of-pairs (BLOSUM62) | Q1, Q2 | [set1_method3_sum_of_pairs.txt](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/results/set1_method3_sum_of_pairs.txt) |
| **results/set1_method4_variance_weighted.txt** | AL2CO Set 1: Weighted variance | Q1, Q2 | [set1_method4_variance_weighted.txt](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/results/set1_method4_variance_weighted.txt) |
| **results/set1_method5_entropy_normalized.txt** | AL2CO Set 1: Normalized entropy | Q1, Q2 | [set1_method5_entropy_normalized.txt](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/results/set1_method5_entropy_normalized.txt) |
| **results/set2_method1_entropy_unweighted.txt** | AL2CO Set 2: Unweighted entropy | Q1, Q2, Q3, Q5 | [set2_method1_entropy_unweighted.txt](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/results/set2_method1_entropy_unweighted.txt) |
| **results/set2_method2_variance_unweighted.txt** | AL2CO Set 2: Unweighted variance | Q1, Q2 | [set2_method2_variance_unweighted.txt](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/results/set2_method2_variance_unweighted.txt) |
| **results/set2_method3_sum_of_pairs.txt** | AL2CO Set 2: Unweighted sum-of-pairs (BLOSUM62) | Q1, Q2 | [set2_method3_sum_of_pairs.txt](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/results/set2_method3_sum_of_pairs.txt) |
| **results/set2_method4_variance_weighted.txt** | AL2CO Set 2: Weighted variance | Q1, Q2 | [set2_method4_variance_weighted.txt](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/results/set2_method4_variance_weighted.txt) |
| **results/set2_method5_entropy_normalized.txt** | AL2CO Set 2: Normalized entropy | Q1, Q2 | [set2_method5_entropy_normalized.txt](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/results/set2_method5_entropy_normalized.txt) |
| **set1_mafft_entropy.txt** | Set 1 MAFFT MSA entropy scores | Q5 | [set1_mafft_entropy.txt](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/set1_mafft_entropy.txt) |
| **set1_muscle_entropy.txt** | Set 1 MUSCLE MSA entropy scores | Q5 | [set1_muscle_entropy.txt](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/set1_muscle_entropy.txt) |
| **set2_mafft_entropy.txt** | Set 2 MAFFT MSA entropy scores | Q5 | [set2_mafft_entropy.txt](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/set2_mafft_entropy.txt) |
| **set2_muscle_entropy.txt** | Set 2 MUSCLE MSA entropy scores | Q5 | [set2_muscle_entropy.txt](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/set2_muscle_entropy.txt) |
| **1BTM.aln** | ConSurf homolog MSA for 1BTM Chain A | Q7 | [1BTM.aln](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/1BTM.aln) |
| **1BTM_A_consurf_grades.txt** | ConSurf conservation grades output | Q7 | [1BTM_A_consurf_grades.txt](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_6/1BTM_A_consurf_grades.txt) |
