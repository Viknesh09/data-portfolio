import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

from xgboost import XGBClassifier
from imblearn.over_sampling import SMOTE

import seaborn as sns
import matplotlib.pyplot as plt

# -----------------------------
# 1. Load Dataset
# -----------------------------
df = pd.read_csv(r"D:\Guvi\Projects\3rd project\EcoType_Project\data\forest_data.csv")

print("Shape:", df.shape)
print(df.head())

# -----------------------------
# 2. Data Cleaning
# -----------------------------
df.drop_duplicates(inplace=True)

# Fill missing values
df.fillna(df.median(numeric_only=True), inplace=True)

# -----------------------------
# 3. Encoding
# -----------------------------
le_wild = LabelEncoder()
le_soil = LabelEncoder()

df['Wilderness_Area'] = le_wild.fit_transform(df['Wilderness_Area'])
df['Soil_Type'] = le_soil.fit_transform(df['Soil_Type'])

joblib.dump(le_wild, "model/le_wilderness.pkl")
joblib.dump(le_soil, "model/le_soil.pkl")

# -----------------------------
# 4. Features & Target
# -----------------------------
X = df.drop("Cover_Type", axis=1)
y = df["Cover_Type"]

# -----------------------------
# 5. Train Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# 6. Handle Imbalance
# -----------------------------
smote = SMOTE(random_state=42)
X_train, y_train = smote.fit_resample(X_train, y_train)

# -----------------------------
# 7. Scaling
# -----------------------------
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

joblib.dump(scaler, "model/scaler.pkl")

# -----------------------------
# 8. Models
# -----------------------------
models = {
    "RandomForest": RandomForestClassifier(),
    "DecisionTree": DecisionTreeClassifier(),
    "LogisticRegression": LogisticRegression(max_iter=200),
    "KNN": KNeighborsClassifier(),
    "XGBoost": XGBClassifier(use_label_encoder=False, eval_metric='mlogloss')
}

best_model = None
best_score = 0

print("\nModel Performance:\n")

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    print(f"{name} Accuracy: {acc:.4f}")

    if acc > best_score:
        best_score = acc
        best_model = model

# -----------------------------
# 9. Hyperparameter Tuning (RandomForest)
# -----------------------------
param_grid = {
    'n_estimators': [100, 200],
    'max_depth': [10, 20]
}

grid = GridSearchCV(RandomForestClassifier(), param_grid, cv=3, n_jobs=-1)
grid.fit(X_train, y_train)

best_model = grid.best_estimator_

# -----------------------------
# 10. Evaluation
# -----------------------------
y_pred = best_model.predict(X_test)

print("\nFinal Model Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

sns.heatmap(cm, annot=True, fmt='d')
plt.title("Confusion Matrix")
plt.show()

# -----------------------------
# 11. Feature Importance
# -----------------------------
importances = best_model.feature_importances_
features = X.columns

plt.figure(figsize=(10,5))
sns.barplot(x=importances, y=features)
plt.title("Feature Importance")
plt.show()

# -----------------------------
# 12. Save Model
# -----------------------------
joblib.dump(best_model, "model/model.pkl")

print("\n✅ Model saved successfully!")