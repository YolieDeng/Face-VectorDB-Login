# Face VectorDB Login v1.0.0
# 创建人：曾逸夫
# 创建时间：2023-12-27
# python face_vectordb_register_cli.py


import cv2
import argparse
from face_vectordb_login_insightface import register


def parse_args(known=False):
    parser = argparse.ArgumentParser(description="Face VectorDB Login v1.0.0")
    parser.add_argument(
        "--username", "-n", default="unknown", type=str, help="register username"
    )
    parser.add_argument(
        "--registerBtn", "-r", default="a", type=str, help="register button"
    )
    parser.add_argument(
        "--fr_mode",
        "-m",
        default="euc",
        type=str,
        help="face recognition mode, default is Euclidean Distance",
    )
    parser.add_argument(
        "--webcam_index", "-wi", default=0, type=int, help="Wencam Index"
    )

    args = parser.parse_known_args()[0] if known else parser.parse_args()
    return args


# webcam 注册
def face_webcam_register(fr_mode, username, registerBtn, webcam_index):
    cap = cv2.VideoCapture(webcam_index)  # 设备连接
    is_capOpened = cap.isOpened()  # 判断摄像头是否正常启动

    if is_capOpened:
        while is_capOpened:
            wait_key = cv2.waitKey(20) & 0xFF  # 键盘监听

            _, frame = cap.read()  # 捕获画面
            cv2.imshow("capture", frame)  # 显示

            if wait_key == ord(registerBtn):
                register(fr_mode, frame, username)
                break

        cap.release()
        cv2.destroyAllWindows()


def main(args):
    username = args.username  # 用户名
    registerBtn = args.registerBtn  # 注册按钮
    fr_mode = args.fr_mode  # 人脸识别模式
    webcam_index = args.webcam_index  # webcam索引

    face_webcam_register(fr_mode, username, registerBtn, webcam_index)


if __name__ == "__main__":
    args = parse_args()
    main(args)
