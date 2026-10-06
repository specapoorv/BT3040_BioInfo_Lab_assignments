# BT3040 - Assignment 9: Sequence Distances & Non-Redundant Databases (CD-HIT & PISCES)

This repository contains the dataset, scripts, non-redundant FASTA databases, cluster files, and comparison analyses for **Assignment 9 (BT3040: Introduction to Bioinformatics)**.

- **Base URL:** [https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9)
- **Questionnaire:** [Assignment 9.pdf](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/Assignment%209.pdf)
- **Report & Solutions:** [Solution 9.pdf](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/Solution%209.pdf)

---

## Quick Summary of Questions & Files

### Q1: Hamming & Euclidean Distance Sequence Comparison
- **Python Distance Script**: [q1.py](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/q1.py)
- **Report & Derivations**: [Solution 9.pdf](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/Solution%209.pdf) (Pages 1–2)

### Q2: CD-HIT Non-Redundant Sets of Transmembrane Beta-Barrels
- **Initial Dataset**: [pdbtm_beta_barrel.fasta](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/pdbtm_beta_barrel.fasta)
- **Result #1 (CD-HIT 90% Cut-off)**:
  - Non-redundant Sequences (398 clusters): [pdbtm_nr90.fasta](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/pdbtm_nr90.fasta)
  - Cluster Details: [pdbtm_nr90.fasta.clstr](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/pdbtm_nr90.fasta.clstr)
- **Result #2 (CD-HIT 75% Cut-off)**:
  - Non-redundant Sequences (354 clusters): [pdbtm_nr75.fasta](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/pdbtm_nr75.fasta)
  - Cluster Details: [pdbtm_nr75.fasta.clstr](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/pdbtm_nr75.fasta.clstr)
- **Result #3 (CD-HIT 50% Cut-off)**:
  - Non-redundant Sequences (280 clusters): [pdbtm_nr50.fasta](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/pdbtm_nr50.fasta)
  - Cluster Details: [pdbtm_nr50.fasta.clstr](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/pdbtm_nr50.fasta.clstr)
- **Result #4 (CD-HIT 40% Cut-off)**:
  - Non-redundant Sequences (251 clusters): [pdbtm_nr40.fasta](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/pdbtm_nr40.fasta)
  - Cluster Details: [pdbtm_nr40.fasta.clstr](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/pdbtm_nr40.fasta.clstr)

### Q3: Comparison of CD-HIT 40% vs 50% Cut-offs
- **50% Non-Redundant Dataset**: [pdbtm_nr50.fasta](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/pdbtm_nr50.fasta)
- **40% Non-Redundant Dataset**: [pdbtm_nr40.fasta](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/pdbtm_nr40.fasta)
- **Comparison & Analysis Tables**: [Solution 9.pdf](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/Solution%209.pdf) (Pages 7–9)

### Q4: Comparison of PDBTM Non-Redundant Set vs CD-HIT 40%
- **Comparison Script**: [q4_compare_fastas.py](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/q4_compare_fastas.py)
- **Input PDBTM Curated NR Set**: [pdbtm_beta_barrel_nr.fasta](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/pdbtm_beta_barrel_nr.fasta)
- **Input CD-HIT 40% NR Set**: [pdbtm_nr40.fasta](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/pdbtm_nr40.fasta)
- **Output Lists**:
  - Overlapping Identifiers (248 IDs): [shared_ids.txt](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/shared_ids.txt)
  - Identifiers Unique to PDBTM (5 IDs): [only_pdbtm_ids.txt](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/only_pdbtm_ids.txt)
  - Identifiers Unique to CD-HIT (3 IDs): [only_cdhit_ids.txt](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/only_cdhit_ids.txt)

### Q5: Non-Redundant Sets using PISCES Server
- **Result #1 (PISCES 20% Identity - 13 chains)**: [cullpdb_pc20.0_res0.0-2.0_len40-10000_R0.25_Xray_d2026_09_30_chains13.fasta](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/cullpdb_pc20.0_res0.0-2.0_len40-10000_R0.25_Xray_d2026_09_30_chains13.fasta)
- **Result #2 (PISCES 30% Identity - 16 chains)**: [cullpdb_pc30.0_res0.0-2.0_len40-10000_R0.25_Xray_d2026_09_30_chains16.fasta](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/cullpdb_pc30.0_res0.0-2.0_len40-10000_R0.25_Xray_d2026_09_30_chains16.fasta)
- **Result #3 (PISCES 40% Identity - 18 chains)**: [cullpdb_pc40.0_res0.0-2.0_len40-10000_R0.25_Xray_d2026_09_30_chains18.fasta](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/cullpdb_pc40.0_res0.0-2.0_len40-10000_R0.25_Xray_d2026_09_30_chains18.fasta)
- **Result #4 (PISCES 50% Identity - 19 chains)**: [cullpdb_pc50.0_res0.0-2.0_len40-10000_R0.25_Xray_d2026_09_30_chains19.fasta](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/cullpdb_pc50.0_res0.0-2.0_len40-10000_R0.25_Xray_d2026_09_30_chains19.fasta)

### Q6: Comparison of PDBTM Non-Redundant Set vs PISCES 40%
- **Comparison Script**: [q6_compare_fastas.py](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/q6_compare_fastas.py)
- **Input PDBTM Curated NR Set**: [pdbtm_beta_barrel_nr.fasta](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/pdbtm_beta_barrel_nr.fasta)
- **Input PISCES 40% NR Set**: [cullpdb_pc40.0_res0.0-2.0_len40-10000_R0.25_Xray_d2026_09_30_chains18.fasta](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/cullpdb_pc40.0_res0.0-2.0_len40-10000_R0.25_Xray_d2026_09_30_chains18.fasta)
- **Report & Analysis**: [Solution 9.pdf](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/Solution%209.pdf) (Pages 12–13)

---

## Detailed Question-by-Question Guide

### Question 1: Sequence Distances (Hamming & Euclidean)
- Three protein sequences with unequal lengths:
  - Sequence 1: 81 aa
  - Sequence 2: 151 aa
  - Sequence 3: 80 aa
- **Methods**:
  - **Hamming Distance**: Sequences are end-padded to equal maximum length to count position-by-position mismatches.
    - *Seq 1 & Seq 3*: 71 mismatches (Normalized: $71 / 81 = 0.8765$) &rarr; **Closest Pair**
    - *Seq 1 & Seq 2*: 146 mismatches (Normalized: $146 / 151 = 0.9669$)
    - *Seq 2 & Seq 3*: 147 mismatches (Normalized: $147 / 151 = 0.9735$)
  - **Euclidean Distance**: Evaluated over 20-dimensional amino acid composition frequency vectors:
    $$d_E(\mathbf{f}_a, \mathbf{f}_b) = \sqrt{\sum_{i=1}^{20} (f_{a,i} - f_{b,i})^2}$$
    - *Seq 1 & Seq 3*: **0.1030** &rarr; **Closest Pair**
    - *Seq 1 & Seq 2*: 0.1260
    - *Seq 2 & Seq 3*: 0.1287
- **Run command**:
  ```bash
  python3 q1.py
  ```

---

### Question 2: CD-HIT Clustering at 90%, 75%, 50%, and 40%
Hierarchical CD-HIT runs on beta-barrel membrane proteins from PDBTM ([`pdbtm_beta_barrel.fasta`](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/pdbtm_beta_barrel.fasta)):
1. **90% Cut-off** (`-c 0.90 -n 5`):
   ```bash
   cd-hit -i pdbtm_beta_barrel.fasta -o pdbtm_nr90.fasta -c 0.90 -n 5 -M 16000 -d 0 -T 8
   ```
   &rarr; **398 clusters**
2. **75% Cut-off** (`-c 0.75 -n 5`):
   ```bash
   cd-hit -i pdbtm_nr90.fasta -o pdbtm_nr75.fasta -c 0.75 -n 5 -M 16000 -d 0 -T 8
   ```
   &rarr; **354 clusters**
3. **50% Cut-off** (`-c 0.50 -n 3`):
   ```bash
   cd-hit -i pdbtm_nr75.fasta -o pdbtm_nr50.fasta -c 0.50 -n 3 -M 16000 -d 0 -T 8
   ```
   &rarr; **280 clusters**
4. **40% Cut-off** (`-c 0.40 -n 2`):
   ```bash
   cd-hit -i pdbtm_nr50.fasta -o pdbtm_nr40.fasta -c 0.40 -n 2 -M 16000 -d 0 -T 8
   ```
   &rarr; **251 clusters**

---

### Question 3: Comparative Analysis (50% vs 40% Cut-offs)
As the sequence identity threshold is relaxed from 50% to 40%:
- The number of representative clusters decreases from **280 to 251** (29 sequences merged into larger clusters).
- The word size parameter $-n$ must be adjusted from 3 to 2 to capture matches at 40% identity.
- Redundancy removed:
  - Going from 75% to 50% eliminated 74 sequences (20.9% reduction).
  - Going from 50% to 40% eliminated 29 sequences (10.4% reduction).
  - Cumulative reduction relative to the 354 NR75 pool reached **29.1%**.
- Highly diverse transmembrane beta-barrel structural families (e.g., 8-stranded OmpA vs 22-stranded TonB-dependent receptors) remain distinct across lower thresholds.

---

### Question 4: PDBTM NR vs CD-HIT 40% Overlap
Script [`q4_compare_fastas.py`](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/q4_compare_fastas.py) compares the curated PDBTM non-redundant database ([`pdbtm_beta_barrel_nr.fasta`](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/pdbtm_beta_barrel_nr.fasta)) against our CD-HIT 40% set ([`pdbtm_nr40.fasta`](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/pdbtm_nr40.fasta)):

- **Total sequences in PDBTM NR**: 253
- **Total sequences in CD-HIT 40%**: 251
- **Shared across both sets**: **248**
- **Unique to PDBTM NR**: 5 (`3t24_B`, `4foz_A`, `4fso_B`, `6z34_A`, `7vku_X`)
- **Unique to CD-HIT 40%**: 3 (`3jqo_L`, `3sy9_B`, `4fsp_A`)
- **Jaccard Similarity**: **96.88%**

The high Jaccard similarity indicates near-perfect concordance, with minimal differences due to representative selection heuristics (greedy longest sequence in CD-HIT vs BLAST/structure alignment in PDBTM).

- **Run command**:
  ```bash
  python3 q4_compare_fastas.py
  ```

---

### Question 5: PISCES Non-Redundant Datasets
Non-redundant sets obtained using the PISCES culled PDB server with parameters:
- Resolution $\le 2.0$ Å
- $R$-factor $\le 0.25$
- Sequence length: 40–10,000 aa
- Structure determination method: X-ray only

| Threshold | Output FASTA File | Number of Chains |
| :---: | :--- | :---: |
| **20%** | [`cullpdb_pc20.0_res0.0-2.0_len40-10000_R0.25_Xray_d2026_09_30_chains13.fasta`](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/cullpdb_pc20.0_res0.0-2.0_len40-10000_R0.25_Xray_d2026_09_30_chains13.fasta) | **13** |
| **30%** | [`cullpdb_pc30.0_res0.0-2.0_len40-10000_R0.25_Xray_d2026_09_30_chains16.fasta`](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/cullpdb_pc30.0_res0.0-2.0_len40-10000_R0.25_Xray_d2026_09_30_chains16.fasta) | **16** |
| **40%** | [`cullpdb_pc40.0_res0.0-2.0_len40-10000_R0.25_Xray_d2026_09_30_chains18.fasta`](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/cullpdb_pc40.0_res0.0-2.0_len40-10000_R0.25_Xray_d2026_09_30_chains18.fasta) | **18** |
| **50%** | [`cullpdb_pc50.0_res0.0-2.0_len40-10000_R0.25_Xray_d2026_09_30_chains19.fasta`](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/cullpdb_pc50.0_res0.0-2.0_len40-10000_R0.25_Xray_d2026_09_30_chains19.fasta) | **19** |

---

### Question 6: PDBTM NR vs PISCES 40% Comparison
Script [`q6_compare_fastas.py`](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/q6_compare_fastas.py) compares PDBTM NR against the PISCES 40% set:
- **PISCES 40% Chains**: 18
- **Shared with PDBTM NR**: **18 out of 18 (100% precision)**
- **Shared Chains**: `1a0s_p`, `1bxw_a`, `1e54_a`, `1fep_a`, `1i78_a`, `1kmo_a`, `1p4t_a`, `1qj8_a`, `1t16_a`, `1thq_a`, `1uyn_x`, `2f1v_a`, `2o4v_a`, `2qdz_a`, `3dwo_a`, `3fid_a`, `4c4v_a`, `4n75_a`
- **Jaccard Similarity**: **7.14%**
  - The low Jaccard value is expected because PISCES enforces stringent experimental quality filters (resolution $\le 2.0$ Å, X-ray only, $R \le 0.25$) discarding lower-resolution X-ray and Cryo-EM models that PDBTM retains.

- **Run command**:
  ```bash
  python3 q6_compare_fastas.py
  ```

---

## Master Table of All Files

| File / Directory | Description | Associated Question | GitHub Link |
| :--- | :--- | :---: | :--- |
| **Assignment 9.pdf** | Assignment prompt & instructions | All | [Assignment 9.pdf](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/Assignment%209.pdf) |
| **Solution 9.pdf** | Assignment report, tables, and discussions | All | [Solution 9.pdf](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/Solution%209.pdf) |
| **q1.py** | Python script calculating Hamming & Euclidean distances | Q1 | [q1.py](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/q1.py) |
| **pdbtm_beta_barrel.fasta** | Complete beta barrel protein sequence dataset from PDBTM | Q2 | [pdbtm_beta_barrel.fasta](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/pdbtm_beta_barrel.fasta) |
| **pdbtm_nr90.fasta** | CD-HIT 90% non-redundant sequences (398 reps) | Q2 | [pdbtm_nr90.fasta](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/pdbtm_nr90.fasta) |
| **pdbtm_nr90.fasta.clstr** | CD-HIT 90% cluster composition file | Q2 | [pdbtm_nr90.fasta.clstr](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/pdbtm_nr90.fasta.clstr) |
| **pdbtm_nr75.fasta** | CD-HIT 75% non-redundant sequences (354 reps) | Q2 | [pdbtm_nr75.fasta](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/pdbtm_nr75.fasta) |
| **pdbtm_nr75.fasta.clstr** | CD-HIT 75% cluster composition file | Q2 | [pdbtm_nr75.fasta.clstr](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/pdbtm_nr75.fasta.clstr) |
| **pdbtm_nr50.fasta** | CD-HIT 50% non-redundant sequences (280 reps) | Q2, Q3 | [pdbtm_nr50.fasta](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/pdbtm_nr50.fasta) |
| **pdbtm_nr50.fasta.clstr** | CD-HIT 50% cluster composition file | Q2, Q3 | [pdbtm_nr50.fasta.clstr](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/pdbtm_nr50.fasta.clstr) |
| **pdbtm_nr40.fasta** | CD-HIT 40% non-redundant sequences (251 reps) | Q2, Q3, Q4 | [pdbtm_nr40.fasta](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/pdbtm_nr40.fasta) |
| **pdbtm_nr40.fasta.clstr** | CD-HIT 40% cluster composition file | Q2, Q3, Q4 | [pdbtm_nr40.fasta.clstr](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/pdbtm_nr40.fasta.clstr) |
| **pdbtm_beta_barrel_nr.fasta** | Curated PDBTM non-redundant beta barrel set | Q4, Q6 | [pdbtm_beta_barrel_nr.fasta](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/pdbtm_beta_barrel_nr.fasta) |
| **q4_compare_fastas.py** | Script comparing PDBTM NR vs CD-HIT 40% sets | Q4 | [q4_compare_fastas.py](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/q4_compare_fastas.py) |
| **shared_ids.txt** | Overlapping sequence IDs between PDBTM NR and CD-HIT 40% | Q4 | [shared_ids.txt](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/shared_ids.txt) |
| **only_pdbtm_ids.txt** | IDs unique to PDBTM NR set | Q4 | [only_pdbtm_ids.txt](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/only_pdbtm_ids.txt) |
| **only_cdhit_ids.txt** | IDs unique to CD-HIT 40% set | Q4 | [only_cdhit_ids.txt](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/only_cdhit_ids.txt) |
| **cullpdb_pc20.0_..._chains13.fasta** | PISCES culled dataset at 20% sequence identity (13 chains) | Q5 | [cullpdb_pc20.0_res0.0-2.0_len40-10000_R0.25_Xray_d2026_09_30_chains13.fasta](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/cullpdb_pc20.0_res0.0-2.0_len40-10000_R0.25_Xray_d2026_09_30_chains13.fasta) |
| **cullpdb_pc30.0_..._chains16.fasta** | PISCES culled dataset at 30% sequence identity (16 chains) | Q5 | [cullpdb_pc30.0_res0.0-2.0_len40-10000_R0.25_Xray_d2026_09_30_chains16.fasta](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/cullpdb_pc30.0_res0.0-2.0_len40-10000_R0.25_Xray_d2026_09_30_chains16.fasta) |
| **cullpdb_pc40.0_..._chains18.fasta** | PISCES culled dataset at 40% sequence identity (18 chains) | Q5, Q6 | [cullpdb_pc40.0_res0.0-2.0_len40-10000_R0.25_Xray_d2026_09_30_chains18.fasta](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/cullpdb_pc40.0_res0.0-2.0_len40-10000_R0.25_Xray_d2026_09_30_chains18.fasta) |
| **cullpdb_pc50.0_..._chains19.fasta** | PISCES culled dataset at 50% sequence identity (19 chains) | Q5 | [cullpdb_pc50.0_res0.0-2.0_len40-10000_R0.25_Xray_d2026_09_30_chains19.fasta](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/cullpdb_pc50.0_res0.0-2.0_len40-10000_R0.25_Xray_d2026_09_30_chains19.fasta) |
| **q6_compare_fastas.py** | Script comparing PDBTM NR vs PISCES 40% sets | Q6 | [q6_compare_fastas.py](https://github.com/specapoorv/BT3040_BioInfo_Lab_assignments/tree/main/assignment_9/q6_compare_fastas.py) |
