# 🍽️ Zomato Restaurant Data Analytics & EDA Pipeline

An exploratory data analysis (EDA) and data preprocessing pipeline built using Python, Pandas, and Seaborn. This project investigates a global dataset of **9,551 restaurants** across multiple countries to uncover insights on pricing, ratings, customer engagement, and restaurant distributions.

---

## 📂 Project Structure

```text
📁 01-zomato-eda-analysis/
│
├── 📄 README.md                  # Project documentation & execution guide
├── 📄 requirements.txt           # Python dependencies
│
├── 📁 data/
│   └── 📁 raw/
│       └── zomato.csv            # Raw Zomato dataset
│
├── 📁 src/                       # Modular Python analysis scripts
│   ├── 01_data_cleaning.py       # Missing value handling & data verification
│   ├── 02_eda_analysis.py        # Univariate & bivariate analysis logic
│   └── 03_outlier_detection.py   # Statistical outlier detection for costs & votes
│
└── 📁 outputs/
    └── 📁 figures/               # Generated charts and visualization artifacts
```

## 📁 Dataset Setup
The raw dataset (`zomato.csv`) is excluded from version control due to file size limits. 

To run the analysis locally:
1. Download the dataset from [Kaggle Zomato Dataset](https://www.kaggle.com/).
2. Place `zomato.csv` inside the `data/raw/` directory.