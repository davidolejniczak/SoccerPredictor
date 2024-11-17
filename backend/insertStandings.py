import pandas as pd

def generate_insert_statements():
    # Load the CSV file
    csv_file_path = "../data/BTTS_Premier_League.csv"  # Adjust relative path as needed
    df = pd.read_csv(csv_file_path)

    table_name = "btts"  # Adjust table name as needed

    # Generate the INSERT statements
    insert_statements = []
    for _, row in df.iterrows():
        values = [
            f"'{value}'" if isinstance(value, str) else value
            for value in row
        ]
        sql = f"INSERT INTO {table_name} VALUES ({', '.join(map(str, values))});"
        insert_statements.append(sql)

    # Save the INSERT statements to a SQL file
    insert_file_path = "../backend/insertTable.sql"  # Adjust relative path as needed
    with open(insert_file_path, "w") as f:
        for statement in insert_statements:
            f.write(statement + "\n")

    print(f"INSERT statements saved to {insert_file_path}")

if __name__ == "__main__":
    generate_insert_statements()
