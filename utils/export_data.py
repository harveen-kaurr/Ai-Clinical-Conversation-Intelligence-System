import pandas as pd

df = pd.read_excel("data/Master_Patient_Data_Final.xlsx")

df = df.rename(
    columns={
        "Patient Name": "patient_name",
        "Gender": "gender",
        "Email": "email",
        "Age": "age",
        "Address": "address",
        "Phone number": "phone_number",
        "Alternate phone Number": "alternate_phone_number",
        "Date of Birth": "date_of_birth",
        "Date of Visiting": "date_of_visiting",
        "Occupation": "occupation",
        "Disease": "disease",
        "Disease_Category": "disease_category"
    }
)

columns_to_keep = [
    "patient_name",
    "gender",
    "email",
    "age",
    "address",
    "phone_number",
    "alternate_phone_number",
    "date_of_birth",
    "date_of_visiting",
    "occupation",
    "disease",
    "disease_category"
]

df = df[columns_to_keep]
df["age"] = (
    pd.to_numeric(
        df["age"],
        errors="coerce"
    )
    .fillna(0)
    .astype(int)
)
df.to_csv(
    "data/patients_import.csv",
    index=False
)

print("Patient import file created successfully")