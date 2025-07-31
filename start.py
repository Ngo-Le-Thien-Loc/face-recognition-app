from facedetect import FaceDetector
import readimg
import readvideo
import readwebcam

def select_input():
    detector = FaceDetector()

    print("Chọn nguồn:")
    print("1 - Ảnh")
    print("2 - Video")
    print("3 - Webcam")
    choice = input("Nhập lựa chọn (1/2/3): ")

    if choice == '1':
        path = input("Nhập đường dẫn ảnh: ")
        readimg.run(path, detector)
    elif choice == '2':
        path = input("Nhập đường dẫn video: ")
        readvideo.run(path, detector)
    elif choice == '3':
        readwebcam.run(detector)
    else:
        print("Lựa chọn không hợp lệ.")
