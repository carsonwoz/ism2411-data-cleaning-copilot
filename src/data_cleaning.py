"""
the purpose of this script is to load a messy sales dataset and applies a 
series of cleaning operations to standardize column names, remove invalid 
values, and ensure the dataset is ready for analysis. The goal is to 
demonstrate a clean Python workflow and responsible use of GitHub Copilot.
"""

import pandas as pd

# --------------------------------------------------------------------
# load_data function
# this function loads a CSV file into a pandas DataFrame.
# Copilot Prompt: "Write a function that loads a CSV file into a pandas DataFrame."
# Why: Separating loading logic makes the script modular and clearer.
# --------------------------------------------------------------------
def load_data(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    return df

# --------------------------------------------------------------------
# clean column function
# Copilot Prompt: "Create a function to clean up column names by stripping 
# whitespace, converting to lowercase, and replacing spaces with underscores."
# Why: The raw file contains inconsistent capitalization and spacing.
# --------------------------------------------------------------------
def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df

# --------------------------------------------------------------------
# function to handle missing values
# Copilot Prompt: "Write a function that fills missing number values and 
# removes rows that are missing product or category names."
# Why: Missing values mess up calculations; and they have to be handled consistently.
# --------------------------------------------------------------------
def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Strip whitespace so blanks become true empty values
    df["prodname"] = df["prodname"].str.strip()
    df["category"] = df["category"].str.strip()

    # Drop rows missing product name or category
    df = df.dropna(subset=["prodname", "category"])

    # Fill missing numeric fields with 0
    df["price"] = df["price"].fillna(0)
    df["qty"] = df["qty"].fillna(0)

    return df

# --------------------------------------------------------------------
# function to remove the invalid rows
# Copilot Prompt: "Write a function that removes rows where the price or 
# quantity is negative."
# Why: Negative values are data-entry errors and should not be calculated.
# --------------------------------------------------------------------
def remove_invalid_rows(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Convert the numeric columns to numbers so that it avoids the string comparison error
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["qty"] = pd.to_numeric(df["qty"], errors="coerce")

    df = df[(df["price"] >= 0) & (df["qty"] >= 0)]
    return df

# --------------------------------------------------------------------
# this is the main execution function
# it calls all the necessary function
# --------------------------------------------------------------------
if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    df_raw = load_data(raw_path)
    df_clean = clean_column_names(df_raw)
    df_clean = handle_missing_values(df_clean)
    df_clean = remove_invalid_rows(df_clean)

    df_clean.to_csv(cleaned_path, index=False)

    print("Cleaning complete. First few rows:")
    print(df_clean.head())