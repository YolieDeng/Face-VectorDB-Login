# Face VectorDB login Flask
# 创建人：邓乙华
# 创建时间：2023-12-28


from flask import Blueprint

fvdb = Blueprint("facevectordb", __name__)

from .views import *
