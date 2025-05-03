# Blockhouse Quant Research Internship Trial Task: Order Flow Imbalances (OFI)

This project implements several Order Flow Imbalance (OFI) features based on the paper  
**"Cross-Impact of Order Flow Imbalance in Equity Markets"** by Cont et al. as part of the recruiting process fot a quant research internship.

---

## Project Structure
```
blockhouse\_trial/
├── main.py                   # Entry point for running OFI calculations
├── requirements.txt          # Python dependencies
├── README.md 
├── ofi\_features/            # Modular implementations of each OFI type
│   ├── \__init\__.py
│   ├── best\_level.py
│   ├── multi\_level.py
│   ├── integrated.py
│   └── cross\_asset.py
│   └── utils.py
├── data/  
│   ├── first\25000\_rows.csv # Provided limit order book 
├── outputs/                  # Output feature files or results
└── report/
    └── ofi\_report.tex       # LaTeX answers to conceptual questions
```
---

## Getting Started

1. Clone the repository:
```
   bash
   git clone <your_repo_url>
   cd blockhouse_trial
```
2. Set up your Python environment (e.g., using `venv`):
```
   bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
```
3. Run the main script:
```
   bash
   python main.py
```
---

## OFI Features Implemented

* `Best-Level OFI`: Based on the top bid and ask
* `Multi-Level OFI`: Uses several depth levels of the order book
* `Integrated OFI`: Aggregated measure of multi-level OFI
* `Cross-Asset OFI`: OFI across different assets

---

## Report

Conceptual answers to theoretical questions are located in
[`report/ofi_report.tex`](report/ofi_report.tex), to be compiled to PDF using LaTeX.

---

## Contact

Author: Suisei Nakagawa

This task is part of the Blockhouse summer 2025 quant research internship recruitment process.

