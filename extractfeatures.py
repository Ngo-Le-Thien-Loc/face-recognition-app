import face_recognition
import cv2

def extract_features(image):
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_image)
    if not face_locations:
        return None

    face_encodings = face_recognition.face_encodings(rgb_image, face_locations)

    if face_encodings:
        return face_encodings[0]  # Chỉ lấy khuôn mặt đầu tiên
    return None
