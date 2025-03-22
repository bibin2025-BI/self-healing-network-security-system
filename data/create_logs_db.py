import sqlite3

def create_logs_db():
    # Connect to SQLite database (creates logs.db if it doesn't exist)
    conn = sqlite3.connect('logs.db')
    cursor = conn.cursor()
    
    # Create a table for logs
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            event_type TEXT,
            message TEXT
        )
    ''')
    
    print("Logs table created successfully.")
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_logs_db()