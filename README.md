# 🚗 AI-Powered Car Valuation Dashboard

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Random%20Forest-orange)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red)

## 📌 Overview
This project is an End-to-End Machine Learning application that predicts the fair market value of used cars. It uses a custom-generated dataset reflecting global market trends and a **Random Forest Regressor** model to estimate prices based on vehicle specifications and condition. 

The project includes a fully interactive web dashboard built with **Streamlit**, allowing users to input car details and get instant AI-driven valuations.

**Live Demo:** [Click here to view the AI Dashboard]([https://car-ai-q4qwtr5nrbjwpve3e6seyv.streamlit.app])

## ⚙️ Features
* **Synthetic Data Generation:** A robust algorithm that creates a realistic 5,000-row dataset (`dataset_creator.py`) factoring in brand base prices, yearly depreciation, mileage deduction, and condition multipliers.
* **Machine Learning Model:** Achieves high accuracy (R2 Score: ~99%) using `scikit-learn`'s Random Forest Regressor (`model_trainer.py`).
* **Interactive Web UI:** A modern, user-friendly dashboard built with `streamlit` for seamless user interaction (`dashboard.py`).

## 🛠️ Tech Stack
* **Language:** Python
* **Data Manipulation:** Pandas
* **Machine Learning:** Scikit-Learn
* **Model Serialization:** Joblib
* **Web Framework:** Streamlit

## 🚀 How to Run Locally
1. Clone the repository:
   ```bash
   git clone [https://github.com/CanCansas/Car-Ai.git](https://github.com/CanCansas/Car-Ai.git)