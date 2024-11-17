import pandas as pd
import psycopg2

def fetch_data_from_db(query, db_params):
    """
    Fetch data from PostgreSQL database.
    """
    connection = None
    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(
            database=db_params["database"],
            user=db_params["user"],
            password=db_params["password"],
            host=db_params["host"],
            port=db_params["port"]
        )
        # Fetch data into a DataFrame
        df = pd.read_sql_query(query, connection)
        return df
    except Exception as e:
        print(f"Database connection or query failed: {e}")
        return None
    finally:
        if connection:
            connection.close()

def preprocess_match_data(btts_df, stats_df, match_team_a, match_team_b):
    """
    Combine team statistics into a single feature set for a match.
    """
    # Log column names for debugging
    print("Stats DataFrame Columns:", stats_df.columns)
    print("BTTS DataFrame Columns:", btts_df.columns)

    # Rename columns for merging
    stats_df = stats_df.rename(columns={"TeamName": "Team"})  # Adjust based on actual column name
    btts_df = btts_df.rename(columns={"TeamName": "Team"})  # Adjust based on actual column name

    # Convert percentages to numeric
    stats_df["WinRate"] = stats_df["W"] / stats_df["MP"]
    btts_df["BTTS"] = btts_df["BTTS"].astype(float)

    # Fetch stats for Team A
    team_a_stats = stats_df[stats_df["Team"] == match_team_a].iloc[0]
    team_a_btts = btts_df[btts_df["Team"] == match_team_a].iloc[0]

    # Fetch stats for Team B
    team_b_stats = stats_df[stats_df["Team"] == match_team_b].iloc[0]
    team_b_btts = btts_df[btts_df["Team"] == match_team_b].iloc[0]

    # Create feature set for the match
    match_features = {
        "TeamA_GF": team_a_stats["GF"],
        "TeamA_GA": team_a_stats["GA"],
        "TeamA_WinRate": team_a_stats["WinRate"],
        "TeamA_BTTS": team_a_btts["BTTS"],
        "TeamB_GF": team_b_stats["GF"],
        "TeamB_GA": team_b_stats["GA"],
        "TeamB_WinRate": team_b_stats["WinRate"],
        "TeamB_BTTS": team_b_btts["BTTS"],
        "Home_Team": 1  # Assuming Team A is the home team
    }
    return pd.DataFrame([match_features])
