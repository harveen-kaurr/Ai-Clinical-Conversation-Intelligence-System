import pandas as pd

df = pd.read_excel("data/Master_Patient_Data_Final.xlsx")

print("\nTotal Records:")
print(len(df))

print("\nColumns:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nDuplicate Phone Numbers:")
print(df["Phone number"].duplicated().sum())

duplicate_phone_records = df[
    df["Phone number"].duplicated(keep=False)
]

print(
    duplicate_phone_records[
        ["Patient Name", "Phone number"]
    ].sort_values("Phone number")

)