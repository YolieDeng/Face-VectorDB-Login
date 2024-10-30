# 向量数据库初始化
# 创建人：曾逸夫
# 创建时间：2023-12-27
# python init_face_vectordb.py


import psycopg

conn = psycopg.connect(
    host="localhost", dbname="postgres", user="postgres", password="pyposeweb"
)

conn.execute("CREATE EXTENSION IF NOT EXISTS vector")

cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS face_login;")

cur.execute(
    "CREATE TABLE face_login (id serial PRIMARY KEY,"
    "username varchar (150) NOT NULL,"
    "face_feature vector NOT NULL);"
)

conn.commit()

cur.close()
conn.close()
