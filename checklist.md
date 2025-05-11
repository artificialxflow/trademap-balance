# Trade Balance Chart Creation Checklist

## 1. Data Preparation
- [ ] Prepare your Excel file with the following columns:
  - Country
  - Import Value (value)
  - Trade Balance (value)
- [ ] Add product title (e.g., "Wood charcoal, incl. shell or nut charcoal, whether or not agglomerated")
- [ ] Add year (e.g., 2024)

## 2. Streamlit App Setup
- [ ] Install required Python packages:
  - `streamlit`
  - `pandas`
  - `matplotlib` or `plotly`
  - `openpyxl` (for Excel support)
- [ ] Create a new Python file for your app (e.g., `app.py`)

## 3. Streamlit App Functionality
- [ ] Build a file uploader in Streamlit to upload the Excel file
- [ ] Read and display the uploaded data using pandas
- [ ] Calculate Export Value as (Import Value + Trade Balance)
- [ ] Generate a clustered column/bar chart for Exports (calculated) and Imports
- [ ] Add a line or bar for Trade Balance (use a distinct color for negative values)
- [ ] Add chart title, axis labels, and legend
- [ ] Display a summary of the overall trade balance (e.g., total negative balance)
- [ ] Allow user to download the chart as an image (optional)

## 4. Review and Finalize
- [ ] Test the app with sample data
- [ ] Ensure all labels, titles, and summaries are clear and accurate
- [ ] Confirm the chart is readable and visually appealing

## 5. Best Practices
- [ ] Use meaningful file and variable names in your code
- [ ] Document your code and app usage in the README.md
- [ ] Save and back up your work

---

**How to Use:**
1. **Install dependencies:**
   ```bash
   pip install streamlit pandas matplotlib openpyxl
   ```
2. **Run the app:**
   ```bash
   streamlit run app.py
   ```
3. **Open the local URL** provided by Streamlit in your browser (usually `http://localhost:8501`).

**Tip:** Streamlit makes it easy to share your app—just run `streamlit run app.py` and follow the local URL, or deploy to Streamlit Cloud for sharing with others. 