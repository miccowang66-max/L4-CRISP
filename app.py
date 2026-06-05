#!/usr/bin/env python3
"""
CRISP-DM Linear Regression & Outlier Detection - Streamlit App
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.linear_model import LinearRegression


st.set_page_config(page_title="CRISP-DM Pipeline", layout="wide")


def sample_parameters(n, a_range, b_range, var_range):
    """Sample model parameters within specified ranges."""
    a = np.random.uniform(a_range[0], a_range[1])
    b = np.random.uniform(b_range[0], b_range[1])
    var = np.random.uniform(var_range[0], var_range[1])
    return n, a, b, var


def generate_dataset(n, a, b, var):
    """Generate synthetic linear data with Gaussian noise."""
    x = np.random.uniform(-10, 10, size=n)
    sigma = np.sqrt(var)
    noise = np.random.normal(0, sigma, size=n)
    y = a * x + b + noise
    df = pd.DataFrame({"x": x, "y": y})
    return df


def train_model(df):
    """Initialize and train a Linear Regression model."""
    model = LinearRegression()
    X = df[["x"]]
    y = df["y"]
    model.fit(X, y)
    a_hat = model.coef_[0]
    b_hat = model.intercept_
    return model, a_hat, b_hat


def evaluate_and_find_outliers(df, model):
    """Calculate residuals and identify top 10 outliers."""
    y_pred = model.predict(df[["x"]])
    df = df.copy()
    df["y_pred"] = y_pred
    df["residual"] = np.abs(df["y"] - y_pred)
    top10 = df.nlargest(10, "residual")
    return df, top10


def create_visualization(df, top10, true_a, true_b, a_hat, b_hat):
    """Generate publication-quality scatter plot."""
    fig, ax = plt.subplots(figsize=(12, 8))

    ax.scatter(df["x"], df["y"], c="steelblue", alpha=0.6, s=40,
               label="Data points", edgecolors="white", linewidth=0.5)

    x_line = np.linspace(df["x"].min(), df["x"].max(), 300)
    y_line = a_hat * x_line + b_hat
    ax.plot(x_line, y_line, color="red", linewidth=3,
            label=f"Fitted: y = {a_hat:.2f}x + {b_hat:.2f}")

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
    return fig


def main():
    st.title("CRISP-DM Linear Regression & Outlier Detection")
    st.markdown("---")

    # Phase 1: Business & Data Understanding - Parameter Configuration
    st.header("Phase 1: Business & Data Understanding")
    st.markdown("Configure the simulation parameters below:")

    col1, col2 = st.columns(2)

    with col1:
        n = st.number_input("Sample size (n)", min_value=10, max_value=1000, value=200, step=10)
        a_min, a_max = st.slider("True slope (a) range", -50.0, 50.0, (-50.0, 50.0))

    with col2:
        b_min, b_max = st.slider("True intercept (b) range", 0.0, 100.0, (0.0, 100.0))
        var_min, var_max = st.slider("Noise variance range", 0.0, 300.0, (0.0, 300.0))

    run_button = st.button("Run Simulation", type="primary", use_container_width=True)

    if run_button:
        # Phase 1: Sample parameters
        n, a, b, var = sample_parameters(n, (a_min, a_max), (b_min, b_max), (var_min, var_max))

        st.success(f"Sampled parameters: n={n}, a={a:.4f}, b={b:.4f}, var={var:.4f}")

        # Phase 2: Data Preparation
        st.header("Phase 2: Data Preparation")
        with st.spinner("Generating dataset..."):
            df = generate_dataset(n, a, b, var)
        st.write(f"Generated {len(df)} data points")
        st.dataframe(df.head(10), use_container_width=True)

        # Phase 3: Modeling
        st.header("Phase 3: Modeling")
        with st.spinner("Training Linear Regression model..."):
            model, a_hat, b_hat = train_model(df)
        st.success("Model trained successfully")

        # Phase 4: Evaluation
        st.header("Phase 4: Evaluation")
        df, top10 = evaluate_and_find_outliers(df, model)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("True Slope (a)", f"{a:.4f}")
        with col2:
            st.metric("Estimated Slope (â)", f"{a_hat:.4f}", delta=f"{a_hat - a:.4f}")
        with col3:
            st.metric("True Intercept (b)", f"{b:.4f}")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Estimated Intercept (b̂)", f"{b_hat:.4f}", delta=f"{b_hat - b:.4f}")
        with col2:
            st.metric("Noise Variance", f"{var:.4f}")
        with col3:
            st.metric("Noise Std Dev (σ)", f"{np.sqrt(var):.4f}")

        st.subheader("Top 10 Outliers")
        st.dataframe(top10[["x", "y", "y_pred", "residual"]], use_container_width=True)

        # Phase 5: Deployment & Visualization
        st.header("Phase 5: Deployment & Visualization")
        fig = create_visualization(df, top10, a, b, a_hat, b_hat)
        st.pyplot(fig)

        st.success("Pipeline execution complete!")


if __name__ == "__main__":
    main()
