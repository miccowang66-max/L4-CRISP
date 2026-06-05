# CRISP-DM Linear Regression & Outlier Detection

<div align="center">

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://l4-crisp.streamlit.app)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/miccowang66-max/L4-CRISP.svg)](https://github.com/miccowang66-max/L4-CRISP/stargazers)

**A complete data mining pipeline following the CRISP-DM framework**  
*Simulate, model, evaluate, and visualize linear regression with outlier detection*

[Live Demo](https://l4-crisp.streamlit.app) • [Report Bug](https://github.com/miccowang66-max/L4-CRISP/issues) • [Request Feature](https://github.com/miccowang66-max/L4-CRISP/issues)

</div>

---

## 🎯 Live Demo

**Try it now:** [https://l4-crisp.streamlit.app](https://l4-crisp.streamlit.app)

The interactive Streamlit app lets you:
- Configure simulation parameters in real-time
- Generate synthetic datasets with custom noise levels
- Train linear regression models instantly
- Visualize outliers with publication-quality plots
- Explore the complete CRISP-DM workflow

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [CRISP-DM Methodology](#-crisp-dm-methodology)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Dependencies](#-dependencies)
- [Screenshots](#-screenshots)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🔍 Overview

This project demonstrates a complete **Cross-Industry Standard Process for Data Mining (CRISP-DM)** workflow applied to linear regression analysis. It generates synthetic data following a linear trend with Gaussian noise, fits a regression model, and identifies the top 10 most anomalous data points.

**Business Objective:**  
Simulate a linear relationship `y = ax + b + ε` where `ε ~ N(0, σ²)`, then use machine learning to recover the true parameters and detect outliers that deviate significantly from the expected baseline.

---

## ✨ Features

- **Dynamic Parameter Sampling**: Randomly sample slope, intercept, and noise variance within configurable ranges
- **Mathematical Precision**: Properly computes σ = √variance before generating Gaussian noise
- **Interactive Visualization**: Publication-quality scatter plots with highlighted outliers
- **Dual Interface**: 
  - CLI script for batch processing
  - Streamlit web app for interactive exploration
- **Comprehensive Reporting**: Formatted console output comparing true vs estimated parameters
- **Top 10 Outlier Detection**: Identifies and ranks data points by absolute residual

---

## 🔄 CRISP-DM Methodology

This project strictly follows the 5 phases of CRISP-DM:

### Phase 1: Business & Data Understanding
- Define objective: Linear regression with outlier detection
- Sample parameters: n=200, a∈[-50,50], b∈[0,100], var∈[0,300]

### Phase 2: Data Preparation
- Generate x: n points uniformly distributed in [-10, 10]
- Generate y: y = ax + b + N(0, σ) where σ = √var
- Structure data in pandas DataFrame

### Phase 3: Modeling
- Initialize scikit-learn LinearRegression
- Train model on prepared dataset
- Extract estimated coefficients: â (slope) and b̂ (intercept)

### Phase 4: Evaluation
- Calculate residuals: |y_actual - y_predicted|
- Rank data points by absolute residual
- Identify top 10 outliers
- Generate comparison report (true vs estimated parameters)

### Phase 5: Deployment & Visualization
- Create scatter plot of complete dataset
- Overlay fitted regression line (red)
- Highlight top 10 outliers (orange, oversized markers)
- Display true vs trained equations in title
- Save publication-quality PNG

---

## 💻 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Clone the Repository
```bash
git clone https://github.com/miccowang66-max/L4-CRISP.git
cd L4-CRISP
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

**Dependencies:**
- streamlit>=1.28.0
- numpy>=1.24.0
- pandas>=2.0.0
- scikit-learn>=1.3.0
- matplotlib>=3.7.0

---

## 🚀 Usage

### Option 1: Streamlit Web App (Recommended)

Launch the interactive web interface:

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

**Features:**
- Interactive sliders for parameter ranges
- One-click simulation execution
- Real-time visualization
- Detailed metrics dashboard
- Top 10 outliers table

### Option 2: Command-Line Interface

Run the batch processing script:

```bash
python crisp_dm_pipeline.py
```

**Output:**
- Console report with true vs estimated parameters
- Top 10 outliers table with coordinates and residuals
- Visualization saved as `crisp_dm_regression_output.png`

**Example Output:**
```
======================================================================
  CRISP-DM EXECUTION REPORT
======================================================================

  Parameter                 True Value       Estimated
  -------------------- --------------- ---------------
  Slope (a)                     2.0560          2.0805
  Intercept (b)                 8.0436          8.3259
  Noise Var                    29.1041             N/A

  Top 10 Outliers (by absolute residual):
  Rank   Index               x            y       y_pred     Residual
  ------ -------- ------------ ------------ ------------ ------------
  1      140           -5.4195     -20.4962      -2.9493      17.5469
  2      195            2.3888      28.2541      13.2957      14.9585
  ...
```

---

## 📁 Project Structure

```
L4-CRISP/
├── app.py                      # Streamlit web application
├── crisp_dm_pipeline.py        # CLI execution script
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore rules
├── LOG.md                      # Development log
├── README.md                   # This file
└── crisp_dm_regression_output.png  # Generated visualization (gitignored)
```

---

## 📊 Screenshots

### Streamlit App Interface
![Streamlit App](https://via.placeholder.com/800x400?text=Streamlit+App+Interface)

### Regression Visualization
![Regression Plot](https://via.placeholder.com/800x600?text=Regression+Visualization+with+Outliers)

*The visualization shows:*
- 🔵 Blue dots: Complete dataset
- 🔴 Red line: Fitted regression line
- 🟠 Orange circles: Top 10 outliers (oversized, high-contrast)

---

## 🧮 Mathematical Details

### Data Generation Formula
```
y = a·x + b + ε
where:
  x ~ Uniform(-10, 10)
  ε ~ N(0, σ)
  σ = √var
```

### Linear Regression Model
```
ŷ = â·x + b̂
where:
  â = estimated slope (model.coef_)
  b̂ = estimated intercept (model.intercept_)
```

### Outlier Detection
```
residual = |y_actual - y_predicted|
outliers = top 10 data points with largest residuals
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 📧 Contact

**GitHub:** [@miccowang66-max](https://github.com/miccowang66-max)  
**Repository:** [L4-CRISP](https://github.com/miccowang66-max/L4-CRISP)  
**Live Demo:** [https://l4-crisp.streamlit.app](https://l4-crisp.streamlit.app)

---

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) - For the amazing web app framework
- [scikit-learn](https://scikit-learn.org/) - For machine learning tools
- [CRISP-DM](https://en.wikipedia.org/wiki/Cross-industry_standard_process_for_data_mining) - For the data mining methodology framework

---

<div align="center">

**If you found this project useful, please consider giving it a ⭐!**

[Back to top](#crisp-dm-linear-regression--outlier-detection)

</div>
