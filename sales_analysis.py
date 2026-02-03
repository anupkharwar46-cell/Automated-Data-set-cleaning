import pandas as pd
import numpy as np

class SalesAnalysisPipeline:

    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None
        self.insights = []

    # -----------------------------
    # 1. Load Data
    # -----------------------------
    def load_data(self):
        self.df = pd.read_csv(self.file_path)

        # DEBUG: show raw columns
        print("RAW COLUMNS:", self.df.columns.tolist())
        return self

    # -----------------------------
    # 2. Standardize Columns
    # -----------------------------
    def standardize_columns(self):
        # clean column names
        self.df.columns = (
            self.df.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
        )

        column_mapping = {
            "order_id": "Order_ID",
            "order_date": "Order_Date",
            "date": "Order_Date",
            "region": "Region",
            "region_name": "Region",
            "item": "Product",
            "product": "Product",
            "quantity": "Quantity",
            "qty": "Quantity",
            "sales": "Revenue",
            "sale": "Revenue",
            "revenue": "Revenue",
            "amount": "Revenue",
            "cost": "Cost"
        }

        self.df.rename(columns=column_mapping, inplace=True)

        # DEBUG: show standardized columns
        print("STANDARDIZED COLUMNS:", self.df.columns.tolist())
        return self

    # -----------------------------
    # 3. Data Cleaning
    # -----------------------------
    def clean_data(self):
        self.df.drop_duplicates(inplace=True)

        for col in ["Region", "Product"]:
            if col in self.df.columns:
                self.df[col] = self.df[col].fillna("Unknown")

        for col in ["Revenue", "Cost", "Quantity"]:
            if col in self.df.columns:
                self.df[col] = self.df[col].fillna(0)

        if "Order_Date" in self.df.columns:
            self.df["Order_Date"] = pd.to_datetime(self.df["Order_Date"], errors="coerce")

        return self

    # -----------------------------
    # 4. Feature Engineering
    # -----------------------------
    def create_features(self):
        if "Cost" in self.df.columns:
            self.df["Profit"] = self.df["Revenue"] - self.df["Cost"]
        else:
            self.df["Profit"] = np.nan

        if "Order_Date" in self.df.columns:
            self.df["Year"] = self.df["Order_Date"].dt.year
            self.df["Month"] = self.df["Order_Date"].dt.month
            self.df["Month_Name"] = self.df["Order_Date"].dt.strftime("%B")

        return self

    # -----------------------------
    # 5. KPI + Insights
    # -----------------------------
    def generate_insights(self):

        if "Revenue" not in self.df.columns:
            raise ValueError(
                f"Revenue column not found. Available columns: {self.df.columns.tolist()}"
            )

        total_revenue = self.df["Revenue"].sum()
        self.insights.append(f"• Total revenue generated is ₹{total_revenue:,.0f}.")

        if "Profit" in self.df.columns:
            total_profit = self.df["Profit"].sum()
            self.insights.append(f"• Total profit earned is ₹{total_profit:,.0f}.")

        if "Product" in self.df.columns:
            top_product = (
                self.df.groupby("Product")["Revenue"].sum().idxmax()
            )
            self.insights.append(f"• Top performing product is '{top_product}'.")

        if "Region" in self.df.columns:
            top_region = (
                self.df.groupby("Region")["Revenue"].sum().idxmax()
            )
            self.insights.append(f"• Highest revenue came from {top_region} region.")

        if {"Year", "Month"}.issubset(self.df.columns):
            monthly_sales = (
                self.df.groupby(["Year", "Month"])["Revenue"]
                .sum()
                .pct_change() * 100
            )

            latest_growth = monthly_sales.iloc[-1]
            if not np.isnan(latest_growth):
                if latest_growth > 0:
                    self.insights.append(
                        f"• Sales increased by {latest_growth:.2f}% compared to previous month."
                    )
                else:
                    self.insights.append(
                        f"• Sales decreased by {abs(latest_growth):.2f}% compared to previous month."
                    )

        return self

    # -----------------------------
    # 6. Export Output
    # -----------------------------
    def export(self,
               cleaned_file="cleaned_sales_data.csv",
               insights_file="insights_report.txt"):

        self.df.to_csv(cleaned_file, index=False)

        with open(insights_file, "w", encoding="utf-8") as f:
            for line in self.insights:
                f.write(line + "\n")

        print("✅ Pipeline executed successfully")
        return self


# -----------------------------
# RUN PIPELINE
# -----------------------------
if __name__ == "__main__":

    pipeline = (
        SalesAnalysisPipeline(r"C:\Users\anup kharwar\OneDrive\Documents\Projects\Automated Sales Data Analysis\raw_data.csv")
        .load_data()
        .standardize_columns()
        .clean_data()
        .create_features()
        .generate_insights()
        .export()
    )
