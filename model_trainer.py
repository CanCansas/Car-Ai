import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib


def train_valuation_model():
    print("Loading the dataset...")
    try:
        df = pd.read_csv("car_prices.csv")
    except FileNotFoundError:
        print("Error: 'car_prices.csv' not found. Run dataset_creator.py first.")
        return

    # 1. Data Preprocessing (Veri Ön İşleme)
    print("Converting categorical data to numerical (One-Hot Encoding)...")
    X = df.drop("Price", axis=1)  # Features (Özellikler: Yıl, KM, Hasar vb.)
    y = df["Price"]  # Target variable (Tahmin etmeye çalıştığımız hedef: Fiyat)

    # Yapay zeka metin anlamaz, o yüzden Marka, Renk gibi metinleri sayılara çeviriyoruz
    X_encoded = pd.get_dummies(X, drop_first=True)

    # 2. Train-Test Split (Verinin %80'i eğitim, %20'si test için ayrılır)
    X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

    # 3. Model Training (Model Eğitimi)
    print("Training the AI model (Random Forest)... This might take a few seconds.")
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # 4. Model Evaluation (Modelin Başarısını Ölçme)
    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    print("\n--- MODEL PERFORMANCE REPORT ---")
    print(f"✅ R2 Score (Accuracy): {r2 * 100:.2f}%")
    print(f"📉 Mean Absolute Error (MAE): ±${mae:.2f}")
    print("--------------------------------\n")

    # 5. Modeli Kaydetme (Daha sonra arayüzde kullanmak için beyin dosyasını kaydediyoruz)
    print("Saving the model's brain...")
    joblib.dump(model, "car_valuation_model.pkl")
    joblib.dump(X_encoded.columns, "model_columns.pkl")
    print("🎉 Success! Model saved successfully.")


if __name__ == "__main__":
    train_valuation_model()