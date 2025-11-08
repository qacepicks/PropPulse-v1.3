import streamlit as st
import pandas as pd
from prop_ev_core import analyze_props

st.set_page_config(page_title="🏀 PropPulse+ Lite", page_icon="🏀", layout="wide")

st.title("🏀 PropPulse+ | NBA Prop EV Analyzer")
st.caption("AI-Powered Expected Value Analysis • Streamlit Cloud Edition")

uploaded = st.file_uploader("📁 Upload your Excel or CSV export", type=["xlsx", "csv"])

if uploaded:
    if uploaded.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded)
    else:
        df = pd.read_csv(uploaded)
        
    result = analyze_props(df)
    st.success(f"✅ Loaded {len(result)} props")

    # Interactive table
    st.dataframe(result, use_container_width=True)

    # Download button
    csv = result.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Download Updated Results", csv, "propulse_results.csv", "text/csv")

else:
    st.info("Upload your latest `export_prizepicks.csv` or `model_output.xlsx` to begin.")
