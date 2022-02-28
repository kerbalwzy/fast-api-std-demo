# -*- coding:utf-8 -*-
# @Author: wzy
# @Time: 2022/2/28
#
"""
数据库迁移使用 alembic
首次执行-安装-生成配置文件与迁移脚本：
pip install alembic
alembic init -t async <script_directory_here>

执行迁移：
alembic revision --autogenerate -m "<commit_notes>"
alembic upgrade head
"""

__all__ = ['sql_session', 'BaseModel']

import time

from sqlalchemy import Column, BIGINT
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

from config import DATABASE_URL

async_engine = create_async_engine(DATABASE_URL)
async_session = sessionmaker(
    class_=AsyncSession,
    autocommit=False,
    autoflush=False,
    bind=async_engine
)

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    create_at = Column(BIGINT, default=int(time.time()))
    update_at = Column(BIGINT, default=int(time.time()), onupdate=int(time.time()))
    delete_at = Column(BIGINT, default=None)

    def keys(self):
        return map(lambda c: c.key, self.__table__.columns)

    def __getitem__(self, key: str):
        return getattr(self, key)


async def sql_session() -> AsyncSession:
    async with async_session() as session:
        yield session


if __name__ == '__main__':
    pass
