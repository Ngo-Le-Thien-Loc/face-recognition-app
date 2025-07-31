import cv2
import os

def run(img_path, face_detector):
    if not os.path.exists(img_path):
        print("Đường dẫn không đúng hoặc file không tồn tại.")
        return

    img = cv2.imread(img_path)
    if img is None:
        print("Không thể đọc ảnh.")
        return

    img = face_detector.detect(img)
    cv2.imshow("Ảnh với nhận diện khuôn mặt", img)

    while True:
        key = cv2.waitKey(0)
        if key == 27:  # ESC
            break
        elif key == ord('s'):
            screenshot_name = os.path.join("Photos", "image_screenshot.jpg")
            cv2.imwrite(screenshot_name, img)
            print(f"Đã lưu ảnh tại: {screenshot_name}")
    cv2.destroyAllWindows()
