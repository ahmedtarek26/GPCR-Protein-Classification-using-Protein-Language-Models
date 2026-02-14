# GPCR Functional Subgroup Classification Project
## Computational Genomics & NLP Analysis

---

## 🎯 Research Question

**"What is the relationship between sequence alignment percentage and functional similarity in G-protein coupled receptors (GPCRs)?"**

### Key Objectives:
1. Calculate multiple distance metrics (sequence identity, MSA-based, embedding-based)
2. Analyze if high sequence alignment (>90%) always indicates same function
3. Identify cases where moderate alignment (70-85%) shows different functions
4. Find interesting cases of convergent evolution or functional divergence
5. Classify GPCRs into 4-5 meaningful functional subgroups

---

## 📚 Methodology Overview

### Three Distance Metrics Approach:
1. **Sequence Identity (Phase 3)** - Simple pairwise % identity
2. **MSA-based Features (Phase 4)** - Multiple Sequence Alignment analysis
3. **Protein LM Embeddings (Phase 5)** - ESM-2/ProtBERT semantic distances

### Compare & Analyze (Phase 6):
- Which metric best predicts functional similarity?
- Does high alignment always mean same function?
- Answer the research question!

### Tools & Methods:
- **Bioinformatics:** BLAST, Multiple Sequence Alignment (MSA), motif detection
- **Protein Language Models:** ESM-2, ProtBERT for semantic embeddings
- **NLP/ML:** Classification, clustering, distance metric comparison
- **Statistical Analysis:** Correlation, hypothesis testing

---

## 📁 Project Structure

```
gpcr-classification/
│
├── data/
│   ├── raw/
│   │   └── beta1.fasta                          # Original BLAST results
│   │
│   └── processed/
│       ├── sequences_parsed.csv                 # Phase 1 output
│       ├── sequences_labeled_classification.csv # Phase 2 output
│       ├── phase3_similarity_results.csv        # Phase 3 output
│       ├── phase4_msa_alignment.aln             # Phase 4 output
│       ├── phase5_embeddings.npy                # Phase 5 output
│       └── final_classification.csv             # Complete results
│
├── notebooks/
│   ├── 01_data_exploration.ipynb        ✅ DONE
│   ├── 02_label_extraction.ipynb        ✅ DONE  
│   ├── 03_similarity_analysis.ipynb     📝 CURRENT ← YOU ARE HERE
│   ├── 04_msa_classification.ipynb      ⏳ TODO - MSA analysis
│   ├── 05_protein_embeddings.ipynb      ⏳ TODO - LM embeddings
│   ├── 06_alignment_function.ipynb      ⏳ TODO - Research question
│   └── 07_visualization.ipynb           ⏳ TODO - Final results
│
├── figures/                             # Generated visualizations
├── README.md                            # This file
└── requirements.txt                     # Dependencies

```

---

## 🔬 Project Phases

### ✅ Phase 1: Data Exploration (COMPLETED)
**Notebook:** `01_data_exploration.ipynb`

**What was done:**
- Loaded 2000 BLAST hits for beta-1 adrenergic receptor (P07550)
- Filtered by quality (length, gaps)
- Detected conserved motifs (DRY, NPxxY)
- Cleaned sequences

**Output:** `sequences_parsed.csv` (1908 sequences)

---

### ✅ Phase 2: Label Extraction (COMPLETED)
**Notebook:** `02_label_extraction.ipynb`

**What was done:**
- Queried UniProt API for annotations
- Extracted functional labels
- Got 425 confirmed adrenergic receptors

**Output:** `sequences_labeled_classification.csv`

**Results:**
- Adrenergic_beta: 372 (19.5%)
- Adrenergic_alpha: 53 (2.8%)  
- Other_ClassA: 1483 (77.7%) ← Need classification

---

### 📝 Phase 3: Similarity Analysis (CURRENT)
**Notebook:** `03_similarity_analysis.ipynb` ← **YOU ARE HERE**

**Objective:** Calculate **Method 1: Sequence Identity** (first distance metric)

**What to do:**
- Calculate pairwise % identity for all sequences
- Find closest match for each unlabeled sequence
- Get basic alignment percentages

**Output:**
- `phase3_similarity_results.csv`
- `phase3_all_sequences_with_similarity.csv`
- Distance metric #1

**Runtime:** 2-3 minutes

**Run:**
```bash
jupyter notebook 03_similarity_analysis.ipynb
```

---

### ⏳ Phase 4: MSA & Classification (NEXT)
**Notebook:** `04_msa_classification.ipynb` (to be created)

**Objective:** Multiple Sequence Alignment + functional classification

**What to do:**
1. **Multiple Sequence Alignment (MSA):**
   - Align all sequences (Clustal Omega / MUSCLE)
   - Identify conserved regions (alignment windows)
   - Extract position-specific features
   - Get **Method 2: MSA-based distances**

2. **Chemistry-based Features:**
   - Amino acid properties (hydrophobicity, charge, size)
   - Binding pocket analysis
   - Physicochemical profiles

3. **Classification:**
   - Classify all 1908 sequences into 4-5 categories
   - Use Phase 3 similarities + MSA features

**Output:**
- MSA alignment file
- Complete classification
- Distance metric #2

**Tools:** Clustal Omega, Biopython

---

### ⏳ Phase 5: Protein Language Model Embeddings (TODO)
**Notebook:** `05_protein_embeddings.ipynb` (to be created)

**Objective:** Generate embeddings and get **Method 3: Embedding distances**

**What to do:**
1. **Generate Embeddings:**
   - ESM-2 (Facebook AI) or ProtBERT embeddings
   - Extract vector representations for all sequences

2. **Calculate Distances:**
   - Cosine similarity between embeddings
   - This is your "PML embedding scale"
   - Distance metric #3

3. **Compare Methods:**
   - Sequence identity vs embedding distance
   - Which predicts function better?

**Output:**
- Embedding vectors (all sequences)
- Distance matrix from embeddings
- Comparison of 3 distance metrics

**Tools:** ESM-2, ProtBERT, PyTorch

---

### ⏳ Phase 6: Alignment vs Function Analysis (TODO)
**Notebook:** `06_alignment_function_analysis.ipynb` (to be created)

**Objective:** **ANSWER YOUR RESEARCH QUESTION!**

**What to do:**
1. **Compare All 3 Distance Metrics:**
   - Sequence identity (Phase 3)
   - MSA-based (Phase 4)
   - Embedding-based (Phase 5)

2. **Analyze Cases:**
   - >90% alignment + same function? (expected)
   - 70-85% alignment + different function? (interesting!)
   - >90% alignment + different function? (very interesting!)

3. **Statistical Analysis:**
   - Correlation: distance vs function
   - Within vs between group distances
   - Test hypotheses

4. **Answer:** Does high alignment = same function?

**Output:**
- Complete research question answer
- Statistical results
- Case studies

---

### ⏳ Phase 7: Visualization & Report (TODO)
**Notebook:** `07_visualization.ipynb` (to be created)

**Deliverables:**
- Scatter plots, heatmaps, dendrograms
- PCA/t-SNE visualizations
- Final report
- Presentation

---

## 📊 Current Status

| Phase | Status | Notebook | Output |
|-------|--------|----------|--------|
| 1: Data Exploration | ✅ Complete | 01_data_exploration.ipynb | sequences_parsed.csv |
| 2: Label Extraction | ✅ Complete | 02_label_extraction.ipynb | sequences_labeled_classification.csv |
| 3: Similarity | 📝 Current | 03_similarity_analysis.ipynb | phase3_*.csv |
| 4: MSA & Classification | ⏳ Todo | 04_msa_classification.ipynb | MSA + classification |
| 5: PLM Embeddings | ⏳ Todo | 05_protein_embeddings.ipynb | Embeddings + distances |
| 6: Analysis | ⏳ Todo | 06_alignment_function.ipynb | Research answer |
| 7: Visualization | ⏳ Todo | 07_visualization.ipynb | Final report |

---

## 🔍 Research Hypotheses

### H1: High Alignment → Same Function
Sequences with >90% identity should have same function.

### H2: Moderate Alignment → Related Function
70-85% identity indicates related but distinct functions.

### H3: Occasional Functional Divergence
Rare cases: high similarity + different function (convergent evolution).

---

## 🛠️ Requirements

```bash
# Core libraries
pandas numpy matplotlib seaborn

# Bioinformatics
biopython

# MSA tools (Phase 4)
# Install: conda install -c bioconda clustalo muscle

# Protein Language Models (Phase 5)
torch transformers fair-esm
# Or: https://github.com/facebookresearch/esm
```

---

## 🚀 Quick Start

### Current Step (Phase 3):
```bash
jupyter notebook 03_similarity_analysis.ipynb
```

Run all cells to calculate similarity scores (~3 minutes).

### Next Steps:
1. Review Phase 3 results
2. Create Phase 4 notebook (MSA)
3. Generate embeddings (Phase 5)
4. Answer research question (Phase 6)

---

## 📈 Expected Outcomes

1. ✅ Complete classification of 1908 sequences
2. ✅ Three distance metrics calculated and compared
3. ✅ Answer: "Does alignment predict function?"
4. ✅ Identify interesting biological cases
5. ✅ Publication-quality analysis

---

## 📝 Key Insights

### Your Whiteboard Notes Translated:
- **"MSA window"** → Phase 4: Multiple Sequence Alignment
- **"PML embedding scale"** → Phase 5: Protein Language Model distances
- **"Compare distance"** → Phase 6: Compare all 3 distance metrics
- **"Chemistry + 4 lines"** → Phase 4: Amino acid properties

### The Strategy:
Not just one method - **compare three different ways** to measure sequence similarity and see which best predicts functional similarity!

---

## 🎯 Current Action

**Run Phase 3 notebook:**
```bash
jupyter notebook 03_similarity_analysis.ipynb
```

This will give you the first distance metric (sequence identity) to compare with MSA and embeddings later!

---

**Last Updated:** February 13, 2026, 11:51 PM CET

**Status:** Phase 3 ready to run

**Next:** Calculate basic sequence similarities, then move to MSA (Phase 4)

---

*Comparing multiple distance metrics to understand the sequence-function relationship in GPCRs.*
