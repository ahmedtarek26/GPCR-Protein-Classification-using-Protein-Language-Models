# GPCR Protein Classification using Protein Language Models

## Project Overview
This project applies Natural Language Processing techniques, specifically Protein Language Models (PLMs), to classify and analyze Class A G-Protein Coupled Receptors (GPCRs). We use transformer-based models to:

1. **Classify GPCR subfamilies** - Distinguish between similar receptor families (e.g., Dopamine vs. Serotonin receptors)
2. **Detect outliers** - Identify misaligned or non-human sequences using perplexity scores
3. **Analyze motifs** - Focus on conserved regions (DRY, NPxxY) to understand sequence-function relationships

---

## Data
- **Source**: Class A GPCR alignment provided by Professor Francesca
- **Format**: FASTA file with aligned protein sequences (UniRef100 IDs)
- **Features**: 
  - 7 transmembrane helices
  - Conserved motifs: DRY (Asp-Arg-Tyr), NPxxY
  - Alignment gaps indicated by dashes (-)

---

## Project Goals

### Task 1: Subfamily Classification
Train a fine-tuned protein language model (ESM-2 or ProtBERT) to classify GPCR sequences into their specific subfamilies.

**Expected Output**: Classification model with confusion matrix showing which families are most similar

### Task 2: Anomaly Detection
Use perplexity scores to identify:
- Misaligned sequences
- Non-human sequences
- Contaminated/outlier data

**Expected Output**: List of outlier sequences with anomaly scores

### Task 3: Motif Analysis
Analyze whether classification can be achieved using only conserved motifs rather than full sequences.

**Expected Output**: Attention visualization showing which residues the model focuses on

---

## Resources & References

### Key Papers
1. **GPCR-BERT: Interpreting Sequential Design of G Protein-Coupled Receptors Using Protein Language Models**
   - Authors: Kim, S., Mathai, P., et al.
   - Journal: *Journal of Chemical Information and Modeling* (2024)
   - DOI: [10.1021/acs.jcim.3c01706](https://pubs.acs.org/doi/10.1021/acs.jcim.3c01706)
   - GitHub: https://github.com/Andrewkimmm/GPCR-BERT
   - **Relevance**: Directly applies BERT to GPCRs, analyzes conserved motifs (NPxxY, CWxP, E/DRY)

2. **Detecting Anomalous Proteins Using Deep Representations**
   - Journal: *PMC* (2024)
   - URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC10939404/
   - **Relevance**: Uses protein language models for anomaly detection, distinguishes viral from host proteins

3. **OD-seq: Outlier Detection in Multiple Sequence Alignments**
   - Journal: *PMC* (2015)
   - URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC4548304/
   - **Relevance**: Classical tool for finding outliers in aligned sequences using gap-based metrics

### Textbook
- **Speech and Language Processing (3rd ed.)** by Jurafsky & Martin
  - Chapters 7-9: Large Language Models, Transformers, Masked Language Models
  - Concepts: Fine-tuning, perplexity, attention mechanisms, embeddings

### Tools & Models
- **ESM-2** (Meta): Pre-trained protein language model
  - Paper: [Evolutionary Scale Modeling](https://github.com/facebookresearch/esm)
- **ProtBERT**: BERT-based protein model
- **UniProt API**: For mapping UniRef IDs to protein families
- **GPCRdb**: GPCR-specific database

---

## Project Structure

```
gpcr-classification/
│
├── data/
│   ├── raw/
│   │   └── beta1.fasta              # Original alignment file
│   ├── processed/
│   │   ├── sequences_labeled.csv    # Sequences with subfamily labels
│   │   └── motifs_extracted.csv     # Extracted DRY/NPxxY regions
│   └── splits/
│       ├── train.csv
│       ├── val.csv
│       └── test.csv
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_label_extraction.ipynb
│   ├── 03_model_training.ipynb
│   └── 04_analysis.ipynb
│
├── src/
│   ├── data_processing.py
│   ├── model.py
│   ├── train.py
│   └── evaluate.py
│
├── results/
│   ├── models/
│   ├── figures/
│   └── metrics/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Getting Started

### Prerequisites
```bash
Python 3.8+
PyTorch
Transformers (HuggingFace)
Biopython
pandas, numpy, matplotlib, seaborn
```

### Installation
```bash
# Clone repository
git clone <repository-url>
cd gpcr-classification

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Quick Start
```bash
# Step 1: Parse FASTA file
python src/data_processing.py --input data/raw/beta1.fasta

# Step 2: Extract labels from UniProt
python src/label_extraction.py

# Step 3: Train model
python src/train.py --model esm2_t6_8M_UR50D --epochs 10

# Step 4: Evaluate and detect outliers
python src/evaluate.py --task classification
python src/evaluate.py --task anomaly_detection
```

---

## Methodology

### Phase 1: Data Preparation ✅ (In Progress)
- [ ] Parse FASTA file and extract sequences
- [ ] Map UniRef IDs to protein subfamilies using UniProt API
- [ ] Filter to top 5-10 most common families
- [ ] Create train/validation/test splits
- [ ] Extract conserved motifs (DRY, NPxxY)

### Phase 2: Model Training
- [ ] Load pre-trained ESM-2 model
- [ ] Add classification head
- [ ] Fine-tune on GPCR subfamily classification
- [ ] Train separate model for motif-only classification

### Phase 3: Outlier Detection
- [ ] Calculate perplexity scores for all sequences
- [ ] Identify high-perplexity outliers
- [ ] Verify if outliers are misaligned or non-human

### Phase 4: Analysis & Visualization
- [ ] Generate confusion matrix
- [ ] Create attention heatmaps
- [ ] Visualize embeddings with t-SNE/UMAP
- [ ] Compare whole-sequence vs. motif-only performance

---

## Key Concepts

| NLP Concept | Protein Application |
|-------------|---------------------|
| Tokenization | Amino acid sequences |
| Masked Language Modeling | Predict masked amino acids |
| Fine-tuning | Adapt to GPCR classification |
| Perplexity | Measure sequence "surprise" for outliers |
| Attention weights | Identify important residues |
| Contextual embeddings | Represent amino acids in context |

---

## Status
**Last Updated**: February 13, 2026

- ✅ Project setup and planning
- ✅ Literature review
- 🔄 Data preprocessing (in progress)
- ⏳ Model training (pending)
- ⏳ Evaluation (pending)
- ⏳ Documentation (pending)

---

## Team
- **Course**: [Course Name]
- **Instructor**: Professor Francesca
- **Date Started**: February 2026

---

## License
[Add your license here]

---

## Acknowledgments
- Professor Francesca for providing the GPCR alignment dataset
- Meta AI for the ESM-2 model
- Authors of GPCR-BERT for methodology inspiration
