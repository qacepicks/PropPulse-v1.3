import pandas as pd

def analyze_props(df):
    """Simplified EV + edge display logic for uploaded prop data."""
    rename = {
        "player": "Player",
        "Player": "Player",
        "stat": "Stat",
        "Stat": "Stat",
        "line": "Line",
        "Line": "Line",
        "projection": "Projection",
        "Projection": "Projection",
        "p_model": "Model Prob",
        "Model_Prob": "Model Prob",
        "p_book": "Book Prob",
        "Book_Prob": "Book Prob",
        "ev": "EV ($/1)",
        "EV": "EV ($/1)",
    }
    df = df.rename(columns=rename)
    for c in ["Model Prob", "Book Prob", "EV ($/1)"]:
        if c not in df.columns:
            df[c] = 0

    # Convert probabilities and EV into readable form
    df["Model Prob"] = (df["Model Prob"] * 100).round(2)
    df["Book Prob"] = (df["Book Prob"] * 100).round(2)
    df["EV (%)"] = (df["EV ($/1)"] * 100).round(2)

    # Simplify key columns for readability
    keep_cols = [
        "Player", "Stat", "Line", "Projection", "Model Prob",
        "Book Prob", "EV (%)"
    ]
    return df[keep_cols].head(100)
