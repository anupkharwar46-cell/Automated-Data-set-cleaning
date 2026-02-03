# Automated-Data-set-cleaning
# Automated Sales Data Analysis Pipeline

## 📌 Project Overview
This project is an end-to-end **sales data analysis pipeline** built using **Python**.  
It automates data loading, cleaning, feature engineering, KPI calculation, and insight generation from raw sales data.

The pipeline converts messy raw data into:
- A **cleaned dataset**
- A **business-ready insights report**

---

## 🛠️ Tools & Technologies
- Python
- pandas
- numpy


---

## 🔄 Pipeline Workflow
The pipeline follows a structured, real-world data analysis process:

1. **Data Loading**
   - Reads raw sales data from CSV file

2. **Column Standardization**
   - Cleans column names
   - Maps inconsistent column names to standard business terms

3. **Data Cleaning**
   - Removes duplicate records
   - Handles missing values
   - Fixes date formats

4. **Feature Engineering**
   - Calculates **Profit**
   - Extracts **Year, Month, and Month Name** from order date

5. **KPI & Insight Generation**
   - Total Revenue
   - Total Profit
   - Top Product
   - Best Performing Region
   - Month-over-Month Sales Growth

6. **Export**
   - Saves cleaned data to CSV
   - Writes insights to a text report

---

## 📊 Key Business Insights
Based on the processed data, the following insights were generated:

- Total revenue generated is **₹1,170,000**
- Total profit earned is **₹349,000**
- Top performing product: **Laptop**
- Highest revenue came from **West** region
- Sales **decreased by 29.41%** compared to the previous month :contentReference[oaicite:0]{index=0}

---

## ▶️ How to Run the Project
1. Install dependencies:
   ```bash
   pip install pandas numpy

   Update the file path of raw_data.csv in sales_analysis.py

2. Run the script:
python sales_analysis.py


3.Output files generated:

   cleaned_sales_data.csv

   insights_report.txt


