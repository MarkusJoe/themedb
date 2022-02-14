#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/14
# @File Name: index.py


import hashlib
import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
async def index():
    return {"code": 200, "msg": "这里是RequestCounter主题数据库下载主页, 下载数据库请前往/assets页面, 获取数据库md5请前往/md5页面", "data": []}


@app.get("/sha256")
async def sha256():
    """
    计算出数据库sha256
    :return: str
    """
    with open("./static/theme.db", "rb") as f:
        data = f.read()
        file_sha256 = hashlib.sha256(data).hexdigest()
        return {'code': 200, 'msg': 'sha256计算成功', 'data': [file_sha256]}



@app.get('/md5')
async def md5():
    """
    计算出数据库md5
    :return: str
     """
    with open("./static/theme.db", 'rb') as fp:
        data = fp.read()
        file_md5 = hashlib.md5(data).hexdigest()
        return {'code': 200, 'msg': 'md5计算成功', 'data': [file_md5]}


@app.get("/assets")
async def assets():
    """
    返回数据库文件
    :return: 
    """
    return FileResponse("./static/theme.db", filename="theme.db")


if __name__ == "__main__":
    uvicorn.run(app="app:app", host="0.0.0.0", port=5000)
