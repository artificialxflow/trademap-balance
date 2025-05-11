import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import io

st.set_page_config(page_title="Trade Balance Chart Generator", layout="wide")
st.title("Trade Balance Chart Generator")

st.markdown("""
Upload your Excel file containing trade data. The file should have the following columns (as exported from TradeMap):
- Importers (Country)
- Value imported in 2024 (USD thousand)
- Trade balance in 2024 (USD thousand)

The app will calculate the Export Value (Import Value + Trade Balance), generate a chart, and display a summary.
""")

uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx", "xls"]) 

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    trademap_cols = {
        "Importers": "Country",
        "Value imported in 2024 (USD thousand)": "Import Value",
        "Trade balance in 2024 (USD thousand)": "Trade Balance"
    }
    if not all(col in df.columns for col in trademap_cols):
        st.error(f"Excel file must contain columns: {', '.join(trademap_cols.keys())}")
    else:
        # Rename columns for internal processing
        df = df.rename(columns=trademap_cols)
        # Calculate Export Value
        df["Export Value"] = df["Import Value"] + df["Trade Balance"]

        st.subheader("Data Preview")
        st.dataframe(df)

        # Plotting (no trend line)
        fig, ax1 = plt.subplots(figsize=(12, 7))
        x = range(len(df["Country"]))
        width = 0.35
        ax1.bar([i - width/2 for i in x], df["Export Value"], width, label="Exports (calculated)", color="green")
        ax1.bar([i + width/2 for i in x], df["Import Value"], width, label="Imports", color="red")
        ax1.set_xticks(list(x))
        ax1.set_xticklabels(df["Country"], rotation=45, ha="right")
        ax1.set_xlabel("Country", fontsize=12, ha='right', labelpad=15)
        ax1.set_ylabel("Value (USD thousand)", fontsize=12, ha='right', labelpad=15)
        plt.title("Trade Balance Chart of Charcoal in 2024", fontsize=14, loc='right')
        ax1.legend(loc="upper left")
        plt.tight_layout()
        st.subheader("Trade Balance Chart")
        st.pyplot(fig)

        # Downloadable PNG
        buf = io.BytesIO()
        fig.savefig(buf, format="png")
        st.download_button(
            label="Download chart as PNG",
            data=buf.getvalue(),
            file_name="trade_balance_chart.png",
            mime="image/png"
        )

        # Downloadable CSV for Excel (matching chart: Country, Export Value, Import Value)
        csv = df[["Country", "Export Value", "Import Value"]].to_csv(index=False)
        st.download_button(
            label="Download data for Excel (CSV)",
            data=csv,
            file_name="trade_balance_data.csv",
            mime="text/csv"
        )

        # Summary
        total_negative = df.loc[df["Trade Balance"] < 0, "Trade Balance"].sum()
        st.info(f"The trade balance for this product was negative in 2024, and imports exceeded exports by ${abs(total_negative):,.0f} (USD thousand).") 