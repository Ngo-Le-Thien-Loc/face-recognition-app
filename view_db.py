import sqlite3
import json
import numpy as np

def view_all_users():
    conn = sqlite3.connect("face_data.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, face_vector FROM users")
    rows = cursor.fetchall()

    if not rows:
        print("CSDL chưa có dữ liệu.")
        return

    print(f"{'ID':<5} {'Tên':<20} {'Vector Length'}")
    print("-" * 50)

    for row in rows:
        user_id, name, vector_str = row
        try:
            vector = np.array(json.loads(vector_str))
            print(f"{user_id:<5} {name:<20} {len(vector)}")
        except Exception as e:
            print(f"Lỗi khi giải mã vector cho {name}: {e}")

    conn.close()

if __name__ == "__main__":
    view_all_users()
