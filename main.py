# -*- coding:utf-8 -*-
# @Author: wzy
# @Time: 2022/2/28
# 

__all__ = []

from fastapi import FastAPI

from routers import sign

app = FastAPI()
app.include_router(sign.router)

if __name__ == '__main__':
    pass
