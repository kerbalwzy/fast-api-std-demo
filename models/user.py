# -*- coding:utf-8 -*-
# @Author: wzy
# @Time: 2022/2/28
# 

__all__ = ['User']

from sqlalchemy import Column, Integer, String, Text

from models import BaseModel


class User(BaseModel):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    account = Column(String(255), nullable=False, doc="账号")
    nickname = Column(String(255), nullable=False, doc="昵称")
    email = Column(String(255), nullable=False, doc="邮箱")
    password = Column(Text, nullable=False, doc="密码HASH")
    avatar = Column(Text, doc="头像链接")
    home_pic = Column(Text, doc="主页背景图片链接")


if __name__ == '__main__':
    pass
