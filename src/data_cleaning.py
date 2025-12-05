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
