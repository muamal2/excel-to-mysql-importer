import pandas as pd
import mysql.connector
from tqdm import tqdm

# Define database connection information for MySQL
db_config = {
    'host': 'host',
    'user': 'user',
    'password': 'password',
    'database': 'database',
}

# Read data from Excel file into a DataFrame using pandas
data = pd.read_excel('example.xls')

# Replace NaN values with 'None'
data.fillna('None', inplace=True)

# Establish connection to MySQL database
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Create the table in the database
create_table_query = """
CREATE TABLE IF NOT EXISTS table_name (
    Name VARCHAR(255) CHARACTER SET utf8mb4,
    city VARCHAR(255) CHARACTER SET utf8mb4,
    status VARCHAR(255) CHARACTER SET utf8mb4,
    phone VARCHAR(255),
    birth DATE,
    number_id INT,
    date DATE
) CHARACTER SET=utf8mb4;

"""
 
# Insert data into MySQL database with progress bar
total_rows = len(data)
inserted_rows = 0  # Track the number of successfully inserted rows
with tqdm(total=total_rows) as pbar:
    for index, row in data.iterrows():
        try:
            query = "INSERT INTO table_name (Name, city, status, phone, birth, number_id, date) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (row['Name'], row['city'], row['status'], row['phone'], row['birth'], row['number_id'], row['date '])
            cursor.execute(query, values)
            inserted_rows += 1
        except Exception as e:
            print(f"Error inserting row {index}: {e}")
        finally:
            pbar.update(1)  # Update progress bar
            pbar.set_description(f"Inserting: {inserted_rows}/{total_rows}")

# Commit the transactions and close the connection
conn.commit()
conn.close()
