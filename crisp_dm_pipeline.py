#!/usr/bin/env python3
"""
CRISP-DM Linear Regression & Outlier Detection Pipeline
"""

# ============================================================================
# PHASE 1: Business & Data Understanding
# ============================================================================

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def sample_parameters():
    """Dynamically sample model parameters within specified ranges."""
    n = 200
    a = np.random.uniform(-50.0, 50.0)
    b = np.random.uniform(0.0, 100.0)
    var = np.random.uniform(0.0, 300.0)
    return n, a, b, var


# ============================================================================
# PHASE 2: Data Preparation
# ============================================================================

def generate_dataset(n, a, b, var):
    """Generate synthetic linear data with Gaussian noise."""
    x = np.random.uniform(-10, 10, size=n)
    sigma = np.sqrt(var)
    noise = np.random.normal(0, sigma, size=n)
    y = a * x + b + noise
    df = pd.DataFrame({"x": x, "y": y})
    return df


# ============================================================================
# PHASE 3: Modeling
# ============================================================================

def train_model(df):
    """Initialize and train a Linear Regression model."""
    model = LinearRegression()
    X = df[["x"]]
    y = df["y"]
    model.fit(X, y)
    a_hat = model.coef_[0]
    b_hat = model.intercept_
    return model, a_hat, b_hat


# ============================================================================
# PHASE 4: Evaluation
# ============================================================================

def evaluate_and_find_outliers(df, model, true_a, true_b, true_var, a_hat, b_hat):
    """Calculate residuals and identify top 10 outliers."""
    y_pred = model.predict(df[["x"]])
    df = df.copy()
    df["y_pred"] = y_pred
    df["residual"] = np.abs(df["y"] - y_pred)
    top10 = df.nlargest(10, "residual")

    print("=" * 70)
    print("  CRISP-DM EXECUTION REPORT")
    print("=" * 70)
    print(f"\n  {'Parameter':<20} {'True Value':>15} {'Estimated':>15}")
    print(f"  {'-'*20} {'-'*15} {'-'*15}")
    print(f"  {'Slope (a)':<20} {true_a:>15.4f} {a_hat:>15.4f}")
    print(f"  {'Intercept (b)':<20} {true_b:>15.4f} {b_hat:>15.4f}")
    print(f"  {'Noise Var':<20} {true_var:>15.4f} {'N/A':>15}")
    print(f"\n  Top 10 Outliers (by absolute residual):")
    print(f"  {'Rank':<6} {'Index':<8} {'x':>12} {'y':>12} {'y_pred':>12} {'Residual':>12}")
    print(f"  {'-'*6} {'-'*8} {'-'*12} {'-'*12} {'-'*12} {'-'*12}")
    for rank, (idx, row) in enumerate(top10.iterrows(), 1):
        print(f"  {rank:<6} {idx:<8} {row['x']:>12.4f} {row['y']:>12.4f} {row['y_pred']:>12.4f} {row['residual']:>12.4f}")
    print("=" * 70)

    return df, top10


# ============================================================================
# PHASE 5: Deployment & Visualization
# ============================================================================

def visualize(df, top10, true_a, true_b, a_hat, b_hat):
    """Generate publication-quality scatter plot with regression line and outliers."""
    fig, ax = plt.subplots(figsize=(12, 8))

    ax.scatter(df["x"], df["y"], c="steelblue", alpha=0.6, s=40, label="Data points", edgecolors="white", linewidth=0.5)

    x_line = np.linspace(df["x"].min(), df["x"].max(), 300)
    y_line = a_hat * x_line + b_hat
    ax.plot(x_line, y_line, color="red", linewidth=3, label=f"Fitted: y = {a_hat:.2f}x + {b_hat:.2f}")

    ax.scatter(top10["x"], top10["y"], c="#FF8C00", s=250, marker="o",
               edgecolors="black", linewidth=1.5, zorder=5, label="Top 10 outliers")

    title = (f"True: y = {true_a:.2f}x + {true_b:.2f}  |  "
             f"Fitted: y = {a_hat:.2f}x + {b_hat:.2f}")
    ax.set_title(title, fontsize=14, fontweight="bold", pad=15)
    ax.set_xlabel("x (Independent Variable)", fontsize=12)
    ax.set_ylabel("y (Dependent Variable)", fontsize=12)
    ax.legend(fontsize=11, loc="best")
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("crisp_dm_regression_output.png", dpi=150)
    plt.close()
    print("\n  Visualization saved to: crisp_dm_regression_output.png")


# ============================================================================
# MAIN EXECUTION PIPELINE
# ============================================================================

def main():
    np.random.seed(None)

    # Phase 1
    n, a, b, var = sample_parameters()
    print(f"\n  Sampled parameters: n={n}, a={a:.4f}, b={b:.4f}, var={var:.4f}\n")

    # Phase 2
    df = generate_dataset(n, a, b, var)

    # Phase 3
    model, a_hat, b_hat = train_model(df)

    # Phase 4
    df, top10 = evaluate_and_find_outliers(df, model, a, b, var, a_hat, b_hat)

    # Phase 5
    visualize(df, top10, a, b, a_hat, b_hat)


if __name__ == "__main__":
    main()
