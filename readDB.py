import sqlite3

def read_database(db_file):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    # Retrieve all table names in the database, excluding "sqlite_sequence"
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name != 'sqlite_sequence';")
    tables = cursor.fetchall()
    
    # Print all tables
    print("Tables in the database:")
    for idx, table in enumerate(tables):
        print(f"{idx + 1}. {table[0]}")
    
    # Ask the user to select a table
    table_index = int(input("Enter the number of the table you want to view: ")) - 1
    selected_table = tables[table_index][0]
    
    # Retrieve and print all data from the selected table
    print(f"\nData from table '{selected_table}':")
    cursor.execute(f"SELECT * FROM {selected_table}")
    rows = cursor.fetchall()
    
    # Print column headers
    column_names = [description[0] for description in cursor.description]
    print("\t".join(column_names))
    
    # Print each row of data
    for row in rows:
        print("\t".join(str(cell) for cell in row))
    
    # Close the connection
    conn.close()

# Call the function and specify the database file name
read_database('questions.db')
