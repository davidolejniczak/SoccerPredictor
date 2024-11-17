import tensorflow as tf
from db_preprocess import preprocess_match_data, fetch_data_from_db

# Database connection parameters
DB_PARAMS = {
    "database": "premierleague_data",
    "user": "postgres",
    "password": "password",
    "host": "localhost",
    "port": "5432"
}

# SQL queries to fetch data
STATS_QUERY = "SELECT * FROM Premier_League_Stats;"
BTTS_QUERY = "SELECT * FROM BTTS_Premier_League;"

def predict_match_winner(model_path, match_team_a, match_team_b):
    """
    Predict the winner of a match.
    """
    # Fetch data from the database
    stats_df = fetch_data_from_db(STATS_QUERY, DB_PARAMS)
    btts_df = fetch_data_from_db(BTTS_QUERY, DB_PARAMS)

    if stats_df is None or btts_df is None:
        print("Failed to fetch data from the database.")
        return

    # Preprocess match data
    match_features = preprocess_match_data(btts_df, stats_df, match_team_a, match_team_b)

    # Load the trained model
    model = tf.keras.models.load_model(model_path)

    # Make predictions
    prediction = model.predict(match_features.values)
    winner = match_team_a if prediction[0][0] > 0.5 else match_team_b
    print(f"Predicted Winner: {winner}")

if __name__ == "__main__":
    predict_match_winner(
        "../models/match_predictor.h5",
        "Liverpool FC",
        "Manchester City FC"
    )
