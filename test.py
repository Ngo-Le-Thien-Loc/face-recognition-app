import sqlite3

# Kết nối đến CSDL (tạo nếu chưa có)
conn = sqlite3.connect("face_data.db")

# Tạo cursor để thao tác SQL
cursor = conn.cursor()

# Tạo bảng users gồm: id, name, face_vector
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        face_vector TEXT NOT NULL
    );
""")

# Lưu thay đổi và đóng kết nối
conn.commit()
conn.close()
