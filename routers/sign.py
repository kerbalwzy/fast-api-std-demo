# -*- coding:utf-8 -*-
# @Author: wzy
# @Time: 2022/2/28
#
__all__ = ['router']

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import or_

from models import sql_session
from models.user import User
from schemas.sign import SignUpParam, SignInParam, SignInResp

router = APIRouter(prefix='/sign', tags=['Sign'])


@router.post('/up', response_model=SignInResp)
async def sign_up(param: SignUpParam, session=Depends(sql_session)):
    # 检查用户邮箱和昵称的可用性
    sql = User.query.filter(or_(User.email == param.email, User.account == param.account))
    res = await session.execute(sql).sac

    return {"id": 1, "email": "kerbalwzy@gmail.com", "nickname": "Test"}


@router.post('/in', response_model=SignInResp)
async def sign_in(param: SignInParam):
    return {"id": 1, "email": "kerbalwzy@gmail.com", "nickname": "Test"}


if __name__ == '__main__':
    pass
