import cv2
import os

def run(video_path, face_detector):
    if not os.path.exists(video_path):
        print("Đường dẫn không đúng hoặc file không tồn tại.")
        return

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Không thể mở video.")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    paused = False
    frame_pos = 0
    screenshot_count = 0

    while True:
        if not paused:
            ret, frame = cap.read()
            if not ret:
                break
            frame_pos = int(cap.get(cv2.CAP_PROP_POS_FRAMES))

        frame_display = face_detector.detect(frame.copy())
        cv2.imshow("Video", frame_display)
        key = cv2.waitKey(30) & 0xFF

        if key == 27:
            break
        elif key == ord('p'):
            paused = not paused
        elif key == ord('s'):
            screenshot_name = os.path.join("Photos", f"screenshot_{screenshot_count}.jpg")
            cv2.imwrite(screenshot_name, frame)
            screenshot_count += 1
        elif key == 83 or key == ord('d'):
            new_frame = min(frame_pos + int(fps * 5), int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1)
            cap.set(cv2.CAP_PROP_POS_FRAMES, new_frame)
        elif key == 81 or key == ord('a'):
            new_frame = max(frame_pos - int(fps * 5), 0)
            cap.set(cv2.CAP_PROP_POS_FRAMES, new_frame)

    cap.release()
    cv2.destroyAllWindows()
