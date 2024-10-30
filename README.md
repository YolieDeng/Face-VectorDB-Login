<p align="center">
<a href="https://gitee.com/intelligence-vision/face-vectordb-login">
<img src="https://pycver.gitee.io/ows-pics/imgs/face-vectordb-login_logo02.png" alt="Simple Icons" >
</a>
<p align="center">
    基于向量数据库的人脸识别注册与登录系统
</p>
</p>
<p align="center">
<a href="./CodeCheck.md"><img src="https://img.shields.io/badge/CodeCheck-passing-success" alt="code check" /></a>
<a href="https://gitee.com/intelligence-vision/face-vectordb-login/releases/v1.0.0"><img src="https://img.shields.io/badge/Releases-v1.0.0-green" alt="Releases Version" /></a>
<a href="https://github.com/pgvector/pgvector"><img src="https://img.shields.io/badge/pgvector-0.5.1%2B-blue?logo=pgvector" alt="pgvector Version" /></a>
<a href="https://github.com/pgvector/pgvector"><img src="https://img.shields.io/badge/pgvector--python-0.2.4%2B-blue?logo=pgvector" alt="pgvector Version" /></a>
<a href="https://www.postgresql.org/"><img src="https://img.shields.io/badge/PostgreSQL-16.1%2B-blue?logo=PostgreSQL" alt="PostgreSQL Version" /></a>
<a href="https://gitee.com/intelligence-vision/face-vectordb-login/blob/master/LICENSE"><img src="https://img.shields.io/badge/License-AGPL--3.0-blue" alt="License" /></a>
</p>
<p align="center">
<a href="https://github.com/deepinsight/insightface"><img src="https://img.shields.io/badge/InsightFace-0.7.3%2B-important?logo=insightface" alt="InsightFace Version" /></a>
<a href="https://github.com/psycopg/psycopg"><img src="https://img.shields.io/badge/psycopg-3.1.16%2B-green?logo=psycopg" alt="psycopg Version" /></a>
<a href="https://www.postgresql.org/"><img src="https://img.shields.io/badge/opencv-4.8.1.78%2B-blue?logo=opencv" alt="OpenCV Version" /></a>
<a href="https://www.postgresql.org/"><img src="https://img.shields.io/badge/flask-3.0.0%2B-blue?logo=flask" alt="Flask Version" /></a>
<a href="https://www.postgresql.org/"><img src="https://img.shields.io/badge/JQuery-3.7.1%2B-blue?logo=jquery" alt="JQuery Version" /></a>
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python" alt="Python Version" /></a>
<a href="https://github.com/SeleniumHQ/selenium"><img src="https://img.shields.io/badge/Selenium-4.16.0%2b-brightgreen?logo=selenium" alt="Selenium Version"></a>
</p>

## 🚀 作者简介

### 👨‍🏫 导师

曾逸夫，从事人工智能研究与开发；主研领域：计算机视觉；[YOLOv8官方开源项目代码贡献人](https://github.com/ultralytics/ultralytics/graphs/contributors)；[YOLOv5官方开源项目代码贡献人](https://github.com/ultralytics/yolov5/graphs/contributors)；[YOLOv5 v6.1代码贡献人](https://github.com/ultralytics/yolov5/releases/tag/v6.1)；[YOLOv5 v6.2代码贡献人](https://github.com/ultralytics/yolov5/releases/tag/v6.2)；[YOLOv5 v7.0代码贡献人](https://github.com/ultralytics/yolov5/releases/tag/v7.0)；[Gradio官方开源项目代码贡献人](https://github.com/gradio-app/gradio/graphs/contributors)

✨  Github：https://github.com/Zengyf-CVer

### 👩‍🎓 学生

邓乙华，从事计算机视觉的研究和JavaScript项目的开发。

<h2 align="center">🚀更新走势</h2>

- `2024-01-01` **⚡ [Face VectorDB Login v1.0.0](https://gitee.com/intelligence-vision/face-vectordb-login/releases/tag/v1.0.0)正式上线**

<h2 align="center">💎项目流程与用途</h2>

### 📌 项目整体流程

<div align="center" >
<img src="https://pycver.gitee.io/ows-pics/imgs/face-vectordb-workflow.png">
</div>

### 📌 项目核心算法与业务流程

<div align="center" >
<img src="https://pycver.gitee.io/ows-pics/imgs/vectordb-face-workflow.png">
</div>

### 📌 Face VectorDB Login Flask 系统界面

#### ❤️ Face VectorDB Login Flask 主页

<div align="center" >
<img src="https://pycver.gitee.io/ows-pics/imgs/face-vectordb-login-flask-index.png">
</div>

#### ❤️ Face VectorDB Login Flask 注册页面

<div align="center" >
<img src="https://pycver.gitee.io/ows-pics/imgs/face-vectordb-login-flask-register.png">
</div>

#### ❤️ Face VectorDB Login Flask 登录页面

<div align="center" >
<img src="https://pycver.gitee.io/ows-pics/imgs/face-vectordb-login-flask-login.png">
</div>

<h2 align="center">💡项目结构</h2>

```
.
├── face-vectordb-login							# 项目名称
│   ├── face-vectordb-login-flask				# Flask Web版
│   │   ├── insightface							# 人脸识别模型目录
│   │   └──└── models		   					# 人脸识别模型
│   │   ├── app									# 蓝图架构
│   │   ├── static								# 静态文件
│   │   ├── templates							# 模板文件
│   │   ├── __init__.py							# 初始化启动文件
│   │   ├── pgsql_config.yaml					# PostgreSQL配置文件
│   │   ├── pgsql_conn.py						# PostgreSQL连接文件
│   │   └── README.md		   					# Flask版项目说明
│   ├── insightface								# 人脸识别模型目录
│   │   └── models		   						# 人脸识别模型
│   ├── pgsql_conn.py							# PostgreSQL数据库连接文件
│   ├── pgsql_config.yaml						# PostgreSQL数据库配置文件
│   ├── init_face_vectordb.py			    	# 向量数据库初始化文件
│   ├── face_vectordb_login_insightface.py		# 项目核心代码
│   ├── face_vectordb_register_cli.py			# CLI注册模块
│   ├── face_vectordb_login_cli.py				# CLI登录模块
│   ├── setup.cfg								# pre-commit CI检查源配置文件
│   ├── .pre-commit-config.yaml					# pre-commit配置文件
│   ├── LICENSE									# 项目许可
│   ├── .gitignore								# git忽略文件
│   ├── README.md								# 项目说明
│   └── requirements.txt						# 脚本依赖文件
```

<h2 align="center">🔥安装教程</h2>

### ✅ 第一步：安装向量数据库

#### ✨ pgvector 安装（Win版）

📌 安装[PostgreSQL](https://www.postgresql.org/)

📌  以管理员身份进入 cmd shell

📌 激活`nmake`

```shell
# 注：改为自己的vcvars64.bat的路径
call "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars64.bat"
```

📌 连接 pgsql 安装目录

```shell
# 注：改为自己的PostgreSQL的路径
set "PGROOT=path\postgres"
```

📌 克隆项目

```shell
git clone --branch v0.5.1 https://github.com/pgvector/pgvector.git
```

📌 编译项目

```shell
cd pgvector
nmake /F Makefile.win
nmake /F Makefile.win install
```

#### ✨ pgvector 安装（Mac版）

📌 安装[PostgreSQL](https://www.postgresql.org/)

📌  在指定conda环境中，安装cmake：`pip install cmake`

📌  配置本地`pg_config`，安装

```shell
# 克隆pgvector项目
git clone --branch v0.5.1 https://github.com/pgvector/pgvector.git
cd pgvector

# 注：改为自己的pg_config路径
export PG_CONFIG=/Library/PostgreSQL/16/bin/pg_config
# 启动root权限安装
sudo --preserve-env=PG_CONFIG make install
```

### ✅ 第二步：下载人脸识别模型

📌 本项目使用[InsightFace](https://insightface.ai/) 的人脸识别模型`buffalo_l`，下载地址：https://github.com/deepinsight/insightface/releases/tag/v0.7

📌 将`buffalo_l.zip`解压到`./insightface/models/`目录下面

📌 将`buffalo_l.zip`解压到`./face-vectordb-login-flask/insightface/models`目录下面

### ✅ 第三步：部署 Face VectorDB Login

📌 创建conda环境

```shell
conda create -n face_vectordb_login python==3.8
conda activate face_vectordb_login # 进入环境
```

📌 克隆face-vectordb-login

```shell
git clone https://gitee.com/intelligence-vision/face-vectordb-login.git
```

📌 安装face-vectordb-login

```shell
cd face-vectordb-login
pip install -r ./requirements.txt -U
```

<h2 align="center">⚡使用教程</h2>

### 💡 Python CLI 版

📌 初始化向量数据库

```shell
# 初始化向量数据库，激活pgvector插件
python init_face_vectordb.py
```

📌 CLI运行注册模块

```shell
# Face vectordb login 注册
python face_vectordb_register_cli.py  # 默认用户名为 unkonwn

python face_vectordb_register_cli.py -n "zengyf"  # 更改用户名为zengyf
python face_vectordb_register_cli.py -n "dengyh"  # 更改用户名为dengyh

python face_vectordb_register_cli.py -r "w"  # 更改注册按钮为w，默认注册按钮为a

python face_vectordb_register_cli.py -m "cos"  # 切换人脸识别模式为 余弦相似度，默认为欧氏距离

python face_vectordb_register_cli.py -wi 1  # 切换摄像头，默认为0
```

📌 CLI运行登录模块

```shell
#  Face vectordb login 登录
python face_vectordb_login_cli.py

python face_vectordb_login_cli.py -l "w"  # 更改登录按钮为w，默认登录按钮为a

python face_vectordb_login_cli.py -m "cos"  # 切换人脸识别模式为 余弦相似度，默认为欧氏距离

python face_vectordb_login_cli.py -wi 1  # 切换摄像头，默认为0
```

### 💡 [Flask Web](https://github.com/pallets/flask) 版

**🔥 本项目采用Flask 3 Blueprints（蓝图）模块化架构**

<div align="center" >
<img src="https://pycver.gitee.io/ows-pics/imgs/face-vectordb-login-flask.png">
</div>

📌 安装 Flask 3.x 框架

```shell
# 切换到yolo环境
conda activate yolo

# 安装Flask Web框架
pip install flask
```

📌 初始化向量数据库

```shell
# 初始化向量数据库，激活pgvector插件
python init_face_vectordb.py
```

📌 运行 Face vectordb login Flask版

```shell
# 在 face-vectordb-login 根目录下启动Flask项目
flask --app face-vectordb-login-flask run
```

### 💡 Selenium自动化测试

📌 自动化运行注册与登录界面

```shell
python face-vectordb-login-selenium/all_seleniunm_fvdbl.py
```

📌 自动化运行注册界面

```shell
python face-vectordb-login-selenium/register_seleniunm_fvdbl.py
```

📌 自动化运行登录界面

```shell
python face-vectordb-login-selenium/login_seleniunm_fvdbl.py
```

### 📝 项目引用指南

📌 如需引用Face VectorDB Login v1.0.0，请在相关文章的**参考文献**中加入下面文字：

```
曾逸夫, 邓乙华 (2024) Face VectorDB Login (Version 1.0.0).https://gitee.com/intelligence-vision/face-vectordb-login.git.
```

### 💬 技术交流

- 如果你发现任何Face VectorDB Login存在的问题或者是建议, 欢迎通过[Gitee Issues](https://gitee.com/intelligence-vision/face-vectordb-login/issues)给我提issues。
- 欢迎加入Intelligence Vision技术交流群

<div align="center" >
<img src="https://pycver.gitee.io/ows-pics/imgs/IntelligenceVisionGroup.jpg" width="20%">
</div>
