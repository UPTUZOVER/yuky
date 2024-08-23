import os
import sqlite3
import time
db_file = 'db.sqlite3'

def create_database():
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_files_to_db(file_names):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    for file_name in file_names:
        try:
            c.execute('INSERT INTO files (name) VALUES (?)', (file_name,))
        except sqlite3.IntegrityError:
            pass

    conn.commit()
    conn.close()
def update_files_in_db(folder_path):
    file_names = os.listdir(folder_path)
    file_names = [f for f in file_names if os.path.isfile(os.path.join(folder_path, f))]
    save_files_to_db(file_names)

def main():
    folder_path = ('media')
    create_database()

    update_files_in_db(folder_path)
    while True:
        update_files_in_db(folder_path)
        time.sleep(2)

if __name__ == "__main__":
    main()
