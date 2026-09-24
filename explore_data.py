from datasets import load_dataset

dataset = load_dataset("scikit-learn/adult-census-income")
df = dataset["train"].to_pandas()

print("Columns:", list(df.columns))
print("\nShape:", df.shape)
print("\nFirst 3 rows:")
print(df.head(3))
print("\nSex values:", df["sex"].unique() if "sex" in df.columns else "no 'sex' column")
