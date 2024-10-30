# Face VectorDB login Flask
# 创建人：邓乙华
# 创建时间：2023-12-28


# 功能模块
from . import fvdb
from flask import render_template, request, session, jsonify
import base64
import cv2
import numpy as np
from .face_vectordb_login_insightface_flask import register_flask, login_flask


# 主页
@fvdb.route("/")
def index():
    user_info = session.get("user_info")
    return render_template("index.html", user_info=user_info)


# 注册
@fvdb.route("/register", methods=["GET", "POST"])
def register():
    user_info = session.get("user_info")

    fr_mode = "euc"

    if request.method == "POST":
        jsonFiles = request.json
        name = jsonFiles["name"]
        base64_frame = jsonFiles["frame"]

        point = base64_frame.find(",")
        base64_str = base64_frame[point + 1 :]
        img_data = base64.b64decode(base64_str)
        img_array = np.fromstring(img_data, np.uint8)
        img = cv2.imdecode(img_array, cv2.COLOR_RGB2BGR)

        result = register_flask(fr_mode, img, name)

        if result == 0:
            return jsonify({"success": True, "message": "注册成功！"})
        elif result == 1:
            return jsonify({"success": True, "message": "未捕捉到人脸信息，注册失败！"})
        elif result == 2:
            return jsonify({"success": True, "message": "用户已存在，请登录！"})
        elif result == 3:
            return jsonify({"success": True, "message": "人脸识别模式错误，程序结束！"})

    return render_template("register.html", user_info=user_info)


# 登录
@fvdb.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    fr_mode = "euc"

    jsonFiles = request.json
    base64_frame = jsonFiles["frame"]

    point = base64_frame.find(",")
    base64_str = base64_frame[point + 1 :]
    img_data = base64.b64decode(base64_str)
    img_array = np.fromstring(img_data, np.uint8)
    img = cv2.imdecode(img_array, cv2.COLOR_RGB2BGR)

    result = login_flask(fr_mode, img)

    if result == 0:
        return jsonify({"success": True, "message": "登录成功！"})
    elif result == 1:
        return jsonify({"success": True, "message": "未捕捉到人脸信息，登录失败！"})
    elif result == 2:
        return jsonify({"success": True, "message": "登录失败！"})
    elif result == 3:
        return jsonify({"success": True, "message": "人脸识别模式错误，程序结束！"})
