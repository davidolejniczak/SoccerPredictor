import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from db_preprocess import preprocess_match_data, fetch_data_from_db
import pandas as pd

# Database connection parameters
DB_PARAMS = {
    "database": "premierleague_data",
    "user": "postgres",
    "password": "password",
    "host": "localhost",
    "port": "5432"
}

# SQL queries to fetch data
STATS_QUERY = "SELECT * FROM standingstats;"
BTTS_QUERY = "SELECT * FROM btts;"

def build_match_prediction_model(input_shape):
    """
    Build a TensorFlow Sequential model for match predictions.
    """
    model = Sequential([
        Dense(64, activation="relu", input_shape=(input_shape,)),
        Dense(32, activation="relu"),
        Dense(1, activation="sigmoid")  # Binary classification
    ])
    return model

def train_match_model():
    """
    Fetch data, preprocess it, and train the TensorFlow model.
    """
    # Fetch data from the database
    stats_df = fetch_data_from_db(STATS_QUERY, DB_PARAMS)
    btts_df = fetch_data_from_db(BTTS_QUERY, DB_PARAMS)

    if stats_df is None or btts_df is None:
        print("Failed to fetch data from the database.")
        return

    # Example match (replace with real data as needed)
    match_team_a = "Leicester City FC"
    match_team_b = "Chelsea FC"

    # Preprocess match data
    match_features = preprocess_match_data(btts_df, stats_df, match_team_a, match_team_b)

    # Create dummy labels for training (1 = Team A wins, 0 = Team B wins)
    X = match_features.values
    y = [1]  # Example label

    # Build and compile the model
    model = build_match_prediction_model(input_shape=X.shape[1])
    model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

    # Train the model
    model.fit(X, y, epochs=10, verbose=1)

    # Save the model
    model.save("../models/match_predictor.h5")
    print("Model saved to ../models/match_predictor.h5")

if __name__ == "__main__":
    train_match_model()
