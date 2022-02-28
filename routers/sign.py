# -*- coding:utf-8 -*-
# @Author: wzy
# @Time: 2022/2/28
#
__all__ = ['router']

from fastapi import APIRouter, HTTPException
from schemas.sign import SignUpParam, SignInParam, SignInResp

router = APIRouter(prefix='/sign', tags=['Sign'])


@router.post('/up', response_model=SignInResp)
async def sign_up(param: SignUpParam):
    return {"id": 1, "email": "kerbalwzy@gmail.com", "nickname": "Test"}


@router.post('/in', response_model=SignInResp)
async def sign_in(param: SignInParam):
    return {"id": 1, "email": "kerbalwzy@gmail.com", "nickname": "Test"}


if __name__ == '__main__':
    pass
