from pathlib import Path

import pandas as pd


folder = Path.cwd() / "data"

initial_version = folder / "Spreadsheet_1.xlsx"
updated_version = folder / "Spreadsheet_2.xlsx"

df_initial = pd.read_excel(initial_version)
df_updated = pd.read_excel(updated_version)

print("Initial shape:", df_initial.shape)
print("Updated shape:", df_updated.shape)
print("Same columns:", df_initial.columns.equals(df_updated.columns))


df_diff = pd.merge(
    df_initial,
    df_updated,
    how="outer",
    indicator="Exist",
)

df_diff = df_diff.query("Exist != 'both'")

print(df_diff)

df_diff.to_excel(folder / "Difference.xlsx", index=False)

