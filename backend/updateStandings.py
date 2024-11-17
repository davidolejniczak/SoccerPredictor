import os
import pandas as pd

def generate_update_statements():
    # File path configuration
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_file_path = os.path.join(project_root, "data", "Premier_League_Stats.csv")
    
    # Load the CSV file
    df = pd.read_csv(csv_file_path)

    # Table name
    table_name = "standings"

    # Unique identifier column (e.g., Position or Team)
    unique_key = "Team"  # Change this if another column is your unique key

    # Generate the UPDATE statements
    update_statements = []
    for _, row in df.iterrows():
        # Extract the unique key value
        unique_key_value = row[unique_key]

        # Generate the SET clause
        set_clause = ", ".join(
            [f"{col} = '{value}'" if isinstance(value, str) else f"{col} = {value}"
             for col, value in row.items() if col != unique_key]
        )

        # Build the UPDATE statement
        sql = f"UPDATE {table_name} SET {set_clause} WHERE {unique_key} = {unique_key_value};"
        update_statements.append(sql)

    # Save to a file or display
    output_file_path = os.path.join(project_root, "backend", "update_statements.sql")
    with open(output_file_path, "w") as f:
        for statement in update_statements:
            f.write(statement + "\n")

    print(f"UPDATE statements saved to {output_file_path}")

if __name__ == "__main__":
    generate_update_statements()
