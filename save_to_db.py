import sqlite3
import numpy as np
import json
import cv2
from extractfeatures import extract_features

def save_face_vector_to_db(img_path, name):
    # Bước 1: Đọc ảnh
    img = cv2.imread(img_path)
    if img is None:
        print("Không đọc được ảnh.")
        return

    # Bước 2: Trích xuất vector đặc trưng
    features = extract_features(img)
    if features is None:
        print("Không tìm thấy khuôn mặt.")
        return

    # Bước 3: Chuyển vector sang JSON
    vector_str = json.dumps(features.tolist())  # Từ np.array → list → json string

    # Bước 4: Ghi vào CSDL
    conn = sqlite3.connect("face_data.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO users (name, face_vector)
        VALUES (?, ?)
    """, (name, vector_str))

    conn.commit()
    conn.close()

    print(f"Đã lưu vector của {name} vào cơ sở dữ liệu.")

# ----------------------------
if __name__ == "__main__":
    img_path = input("Nhập đường dẫn ảnh: ")
    name = input("Nhập tên người: ")
    save_face_vector_to_db(img_path, name)
