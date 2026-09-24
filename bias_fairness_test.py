import pandas as pd
from datasets import load_dataset
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# ---- 1. Load data ----
dataset = load_dataset("scikit-learn/adult-census-income")
df = dataset["train"].to_pandas()
df["income"] = df["income"].astype(str).str.strip()
df["target"] = (df["income"] == ">50K").astype(int)

feature_cols = [
    "age", "workclass", "education", "education.num",
    "marital.status", "occupation", "relationship",
    "race", "sex", "capital.gain", "capital.loss",
    "hours.per.week", "native.country",
]

# ---- 2. Encode categorical columns ----
encoders = {}
X = df[feature_cols].copy()
for col in X.columns:
    if X[col].dtype == object:
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col].astype(str))
        encoders[col] = le

y = df["target"]

# ---- 3. Train/test split, train model ----
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

acc = accuracy_score(y_test, model.predict(X_test))
print(f"Baseline model accuracy: {acc:.3f}")

# ---- 4. Helpers for building a single test profile ----
def make_profile(**kwargs):
    row = {}
    for col in feature_cols:
        val = kwargs[col]
        if col in encoders:
            val = encoders[col].transform([str(val)])[0]
        row[col] = val
    return pd.DataFrame([row])[feature_cols]

def predict_label(row_df):
    pred = model.predict(row_df)[0]
    proba = model.predict_proba(row_df)[0][1]
    return (">50K" if pred == 1 else "<=50K"), proba

base_profile = dict(
    age=37, workclass="Private", education="Bachelors",
    **{"education.num": 13, "marital.status": "Married-civ-spouse",
       "capital.gain": 0, "capital.loss": 0, "hours.per.week": 40,
       "native.country": "United-States"},
    occupation="Exec-managerial", relationship="Husband",
    race="White", sex="Male",
)

# ---- BIA test 1: same profile, only SEX changes ----
print("\n--- BIA test 1: sex (Male vs Female), everything else identical ---")
male_profile = dict(base_profile)
female_profile = dict(base_profile, sex="Female")

male_pred, male_p = predict_label(make_profile(**male_profile))
female_pred, female_p = predict_label(make_profile(**female_profile))
print(f"Male   -> {male_pred} (P(>50K)={male_p:.3f})")
print(f"Female -> {female_pred} (P(>50K)={female_p:.3f})")
print("SAME prediction" if male_pred == female_pred else ">>> DIFFERENT prediction -- possible bias")

# ---- BIA test 2: same profile, only AGE changes ----
print("\n--- BIA test 2: age (25 vs 65), everything else identical ---")
young_profile = dict(base_profile, age=25)
old_profile = dict(base_profile, age=65)

young_pred, young_p = predict_label(make_profile(**young_profile))
old_pred, old_p = predict_label(make_profile(**old_profile))
print(f"Age 25 -> {young_pred} (P(>50K)={young_p:.3f})")
print(f"Age 65 -> {old_pred} (P(>50K)={old_p:.3f})")
print("SAME prediction" if young_pred == old_pred else "DIFFERENT prediction (age legitimately affects income, less concerning)")

# ---- Aggregate fairness metric across the whole test set ----
test_df = X_test.copy()
test_df["pred"] = model.predict(X_test)
test_df["sex_label"] = encoders["sex"].inverse_transform(test_df["sex"])
rates = test_df.groupby("sex_label")["pred"].mean()

print("\n--- Demographic parity across test set (share predicted >50K) ---")
print(rates)
print(f"Gap (Male - Female): {rates.get('Male', 0) - rates.get('Female', 0):.3f}")
