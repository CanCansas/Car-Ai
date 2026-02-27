import pandas as pd
import random

# Global Market Data (Prices in USD)
BRANDS = {
    "Toyota Corolla": {"base_price": 22000, "year_multiplier": 1500},
    "Honda Civic": {"base_price": 24000, "year_multiplier": 1600},
    "Ford Focus": {"base_price": 21000, "year_multiplier": 1400},
    "BMW 3 Series": {"base_price": 45000, "year_multiplier": 3000},
    "Volkswagen Golf": {"base_price": 25000, "year_multiplier": 1700},
    "Fiat Tipo": {"base_price": 18000, "year_multiplier": 1200},
    "Tesla Model 3": {"base_price": 40000, "year_multiplier": 2500}
}

COLORS = ["White", "Black", "Gray", "Red", "Blue"]
TRANSMISSIONS = ["Manual", "Automatic"]
CONDITIONS = ["Clean Title", "Minor Scratches", "Repaired", "Salvage"]


def generate_dataset(num_rows=5000):
    data = []
    print(f"Generating {num_rows} vehicle records for the global dataset...")

    for _ in range(num_rows):
        brand = random.choice(list(BRANDS.keys()))
        year = random.randint(2015, 2024)

        age = 2025 - year
        mileage = random.randint(8000, 15000) * age

        color = random.choice(COLORS)
        transmission = random.choice(TRANSMISSIONS)
        condition = random.choice(CONDITIONS)
        horsepower = random.randint(100, 300)

        # --- PRICE ALGORITHM ---
        base_price = BRANDS[brand]["base_price"]
        year_added = (year - 2015) * BRANDS[brand]["year_multiplier"]
        mileage_deduction = mileage * 0.10

        condition_multiplier = 1.0
        if condition == "Minor Scratches":
            condition_multiplier = 0.90
        elif condition == "Repaired":
            condition_multiplier = 0.80
        elif condition == "Salvage":
            condition_multiplier = 0.50

        transmission_added = 1500 if transmission == "Automatic" else 0

        raw_price = (base_price + year_added + transmission_added - mileage_deduction) * condition_multiplier
        fluctuation = random.uniform(0.95, 1.05)
        final_price = int(raw_price * fluctuation)

        if final_price < 2000: final_price = 2000

        data.append([brand, year, mileage, transmission, horsepower, condition, color, final_price])

    df = pd.DataFrame(data,
                      columns=["Brand", "Year", "Mileage", "Transmission", "Horsepower", "Condition", "Color", "Price"])
    df.to_csv("car_prices.csv", index=False)
    print("✅ 'car_prices.csv' successfully created!")
    return df


if __name__ == "__main__":
    generate_dataset()