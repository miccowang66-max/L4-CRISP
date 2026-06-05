# 📊 CRISP-DM Linear Regression & Outlier Detection

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://l4crispdd.streamlit.app/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](LICENSE)

> A complete data mining pipeline following the CRISP-DM framework.
> **Simulate, model, evaluate, and visualize linear regression with outlier detection.**

---

## 🌐 Live Demo

| Platform | URL | Description |
| --- | --- | --- |
| **Streamlit Cloud** | [l4crispdd.streamlit.app](https://l4crispdd.streamlit.app/) | Interactive web app — configure & run in real-time |

---

## ✨ Features

### Pipeline

- 🔄 **5-Phase CRISP-DM** — Business Understanding → Data Preparation → Modeling → Evaluation → Visualization
- 📐 **Mathematical Rigor** — Proper variance-to-std-dev conversion (σ = √var) for noise generation
- 🎯 **Outlier Detection** — Ranks data points by absolute residual to identify top 10 extreme deviations
- 📊 **Publication-Quality Plots** — Scatter plots with regression line and highlighted outliers

### Interface

| Mode | Description |
| --- | --- |
| **Streamlit Web App** | Interactive sliders, one-click simulation, real-time visualization |
| **CLI Script** | Batch processing with formatted console report |

### Interactive Elements

- 🎚 **Parameter Sliders** — Adjust slope, intercept, noise variance, and sample size
- 📈 **Live Visualization** — Instant plot updates on each simulation run
- 📋 **Metrics Dashboard** — True vs estimated parameter comparison
- 🏷 **Outlier Table** — Ranked list of top 10 anomalies with coordinates & residuals

---

## 🚀 Deployment

### Streamlit Cloud Auto-Deploy

Push to `main` branch triggers automatic redeployment on Streamlit Cloud.

```bash
git push origin main
```

App URL: [https://l4crispdd.streamlit.app/](https://l4crispdd.streamlit.app/)

---

## 🔧 Local Development

```bash
# Clone the repository
git clone https://github.com/miccowang66-max/L4-CRISP.git
cd L4-CRISP

# Install dependencies
pip install -r requirements.txt

# Launch the Streamlit app
streamlit run app.py

# Or run the CLI pipeline
python crisp_dm_pipeline.py
```

> No build tools required. Tailwind CSS is loaded via CDN.

---

## 📁 Project Structure

```
L4-CRISP/
├── app.py                          # Streamlit web application
├── crisp_dm_pipeline.py            # CLI execution script
├── requirements.txt                # Python dependencies
├── .gitignore                      # Git ignore rules
├── LOG.md                          # Development log
├── README.md                       # This file
└── crisp_dm_regression_output.png  # Generated visualization (gitignored)
```

---

## 🛠 Tech Stack

| Technology | Purpose |
| --- | --- |
| [Python 3.8+](https://www.python.org) | Core language |
| [NumPy](https://numpy.org) | Numerical computation & data generation |
| [Pandas](https://pandas.pydata.org) | Data structuring & manipulation |
| [scikit-learn](https://scikit-learn.org) | Linear regression modeling |
| [Matplotlib](https://matplotlib.org) | Publication-quality visualization |
| [Streamlit](https://streamlit.io) | Interactive web application framework |

---

## 🔄 CRISP-DM Methodology

| Phase | Description |
| --- | --- |
| **1. Business Understanding** | Define objective — linear regression with outlier detection. Sample parameters: n=200, a∈[-50,50], b∈[0,100], var∈[0,300] |
| **2. Data Preparation** | Generate x: 200 points ~ Uniform(-10, 10). Generate y: y = ax + b + N(0, σ) where σ = √var. Structure in Pandas DataFrame |
| **3. Modeling** | Initialize scikit-learn LinearRegression. Train on prepared dataset. Extract â (slope) and b̂ (intercept) |
| **4. Evaluation** | Calculate residuals: \|y_actual - y_predicted\|. Rank by absolute residual. Identify top 10 outliers. Compare true vs estimated parameters |
| **5. Visualization** | Scatter plot of full dataset. Overlay fitted regression line (red). Highlight top 10 outliers (orange, oversized markers). Save publication-quality PNG |

---

## 🎨 Customization

| Element | How to Change |
| --- | --- |
| **Sample size** | Adjust `n` slider in Streamlit app or `crisp_dm_pipeline.py` |
| **Parameter ranges** | Edit slider min/max in `app.py` sidebar |
| **Outlier count** | Modify top-K value in evaluation phase |
| **Plot style** | Update Matplotlib styling in `crisp_dm_pipeline.py` |
| **App layout** | Edit Streamlit components in `app.py` |

---

## 📄 License

MIT © [miccowang66-max](https://github.com/miccowang66-max)
