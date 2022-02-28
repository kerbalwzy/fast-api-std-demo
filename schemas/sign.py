# -*- coding:utf-8 -*-
# @Author: wzy
# @Time: 2022/2/28
#
__all__ = ['SignUpParam', 'SignInParam', 'SignInResp']

from pydantic import BaseModel, validator, validate_email


class SignUpParam(BaseModel):
    email: str
    password: str
    password_confirm: str
    avatar: str = None

    @validator('email')
    def check_email(cls, v):
        _, email = validate_email(v)
        return email


class SignInParam(BaseModel):
    email: str
    password: str

    @validator('email')
    def check_email(cls, v):
        _, email = validate_email(v)
        return email


class SignInResp(BaseModel):
    id: int
    email: str
    nickname: str
    avatar: str = None


if __name__ == '__main__':
    pass
