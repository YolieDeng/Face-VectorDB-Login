# Face VectorDB Login Flask v1.0.0
# 创建人：曾逸夫
# 创建时间：2023-12-27
# python face_login_insightface.py


import numpy as np
from sklearn import preprocessing
from insightface.app import FaceAnalysis
from pgsql_conn import get_db_connection


model = FaceAnalysis(
    root="./insightface",
    allowed_modules=["detection", "recognition"],
    providers=["CPUExecutionProvider"],
)

model.prepare(ctx_id=-1, det_thresh=0.5, det_size=(640, 640))


# 注册模块
# 0: 注册成功！
# 1: 未捕捉到人脸信息，注册失败！
# 2: 用户已存在，请登录！
# 3: 人脸识别模式错误，程序结束！
def register_flask(fr_mode, image, username):
    faces = model.get(img=image)
    if len(faces) != 1:
        print("未捕捉到人脸信息，注册失败！")
        return 1

    embedding = np.array(faces[0].embedding).reshape((1, -1))
    embedding = preprocessing.normalize(embedding)[0]

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM face_login")
    res = cur.fetchall()

    if res:
        for i in range(len(res)):
            if fr_mode == "euc":
                distance = cur.execute(
                    "SELECT * FROM face_login WHERE face_feature <-> %s < 1.24",
                    (embedding,),
                ).fetchall()
            elif fr_mode == "cos":
                distance = cur.execute(
                    "SELECT * FROM face_login WHERE face_feature <=> %s < 1.24",
                    (embedding,),
                ).fetchall()
            else:
                print("人脸识别模式错误，程序结束！")
                return 3

            conn.commit()

            if distance:
                print("用户已存在，请登录！")
                return 2
            else:
                cur.execute(
                    f"INSERT INTO face_login (username,face_feature) VALUES (%s,%s)",
                    (
                        username,
                        embedding,
                    ),
                )
                conn.commit()
                cur.close()
                conn.close()
                print(f"{username} 注册成功！")
                return 0

    else:
        cur.execute(
            f"INSERT INTO face_login (username,face_feature) VALUES (%s,%s)",
            (
                username,
                embedding,
            ),
        )
        conn.commit()
        cur.close()
        conn.close()

        print(f"{username} 注册成功！")
        return 0


# 登录模块
# 0: 登录成功！
# 1: 未捕捉到人脸信息，登录失败！
# 2: 登录失败！
# 3: 人脸识别模式错误，程序结束！
def login_flask(fr_mode, image):
    faces = model.get(img=image)
    if len(faces) != 1:
        print("未捕捉到人脸信息，登录失败！")
        return 1

    embedding = np.array(faces[0].embedding).reshape((1, -1))
    embedding = preprocessing.normalize(embedding)[0]
    distance = None

    conn = get_db_connection()
    cur = conn.cursor()

    if fr_mode == "euc":
        distance = cur.execute(
            "SELECT username FROM face_login WHERE face_feature <-> %s < 1.24",
            (embedding,),
        ).fetchall()
    elif fr_mode == "cos":
        distance = cur.execute(
            "SELECT username FROM face_login WHERE face_feature <-> %s < 1.24",
            (embedding,),
        ).fetchall()
    else:
        print("人脸识别模式错误，程序结束！")
        return 3

    conn.commit()

    if distance:
        username = distance[0][0]
        print(f"{username} 登录成功！")
        cur.close()
        conn.close()

        return 0
    else:
        print("登录失败！")
        cur.close()
        conn.close()

        return 2
