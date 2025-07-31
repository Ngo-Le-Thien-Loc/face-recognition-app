import cv2
import os

def run(face_detector):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Không thể mở webcam.")
        return

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = 20
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(os.path.join("Videos", "output.avi"), fourcc, fps, (width, height))

    screenshot_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = face_detector.detect(frame)
        out.write(frame)
        cv2.imshow("Webcam", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == 27:
            break
        elif key == ord('s'):
            screenshot_name = os.path.join("Photos", f"webcam_screenshot_{screenshot_count}.jpg")
            cv2.imwrite(screenshot_name, frame)
            screenshot_count += 1

    cap.release()
    out.release()
    cv2.destroyAllWindows()
