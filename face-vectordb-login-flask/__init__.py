# Face VectorDB login Flask
# 创建人：邓乙华
# 创建时间：2023-12-28
# flask --app face-vectordb-login-flask run


from flask import Flask
from .app.FVflask_usermode import views as fv
from flask_cors import CORS


def create_app():
    app = Flask(__name__)

    # --------- 自动更新前后端 ---------
    app.jinja_env.auto_reload = True
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.secret_key = "QWERTYUIOP"  # 对用户信息加密

    app.register_blueprint(fv.fvdb, url_prefix="/fvdb")
    app.add_url_rule("/", endpoint="index", view_func=fv.index)

    CORS(app)  # 跨域
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
