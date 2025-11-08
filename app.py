import streamlit as st
import pandas as pd
from prop_ev_core import run_prop_ev

st.set_page_config(page_title="🏀 PropPulse+ Lite", page_icon="🏀", layout="centered")

st.title("🏀 PropPulse+ Lite")
st.caption("AI-Powered EV Analyzer | Fully Automated Opponent + Home/Away Detection")

mode = st.radio("Select Mode:", ["Single Prop", "Batch Mode"], horizontal=True)

if mode == "Single Prop":
    st.subheader("Enter a Prop")
    player = st.text_input("Player Name", placeholder="e.g. Tyrese Maxey")
    stat = st.selectbox("Stat Type", ["PTS", "REB", "AST", "PRA", "REB+AST", "FG3M"])
    line = st.number_input("Prop Line", step=0.5)
    odds = st.number_input("Sportsbook Odds (e.g. -110)", value=-110)

    if st.button("Run Model"):
        with st.spinner("Analyzing prop..."):
            result = run_prop_ev(player, stat, line, odds)
            if result is not None:
                st.success("✅ Model Complete")
                st.json(result)
            else:
                st.error("⚠️ Could not fetch player or matchup data. Try again.")

else:
    st.subheader("Batch Mode (Multiple Props)")
    st.caption("Paste one per line: Player,Stat,Line,Odds")
    user_input = st.text_area(
        "Enter multiple props:",
        height=200,
        placeholder="e.g.\nCade Cunningham,PTS,21.5,-110\nScottie Barnes,REB,8.5,-115"
    )

    if st.button("Run Batch"):
        lines = [x.strip() for x in user_input.split("\n") if x.strip()]
        results = []
        with st.spinner("Running batch model..."):
            for l in lines:
                try:
                    player, stat, line, odds = [x.strip() for x in l.split(",")]
                    result = run_prop_ev(player, stat, float(line), float(odds))
                    results.append(result)
                except Exception as e:
                    results.append({"Player": l, "Error": str(e)})

        df = pd.DataFrame(results)
        st.dataframe(df, use_container_width=True)
