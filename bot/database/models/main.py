from aiogram import types
from gino import Gino
import datetime
from gino.schema import GinoSchemaVisitor
from sqlalchemy import (Column, Integer, BigInteger, String,
                        Sequence, TIMESTAMP, )
from sqlalchemy import sql
from bot.misc import TgKeys

db_pass = TgKeys.DB_PASS
db_user = TgKeys.DB_USER
db_name = TgKeys.DB_NAME
host = TgKeys.host
db = Gino()


# Документация
# http://gino.fantix.pro/en/latest/tutorials/tutorial.html

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    user_id = Column(BigInteger)
    time = Column(TIMESTAMP)
    full_name = Column(String(100))
    username = Column(String(50))
    query: sql.Select

    def __repr__(self):
        return "<User(id='{}', fullname='{}', username='{}')>".format(
            self.id, self.full_name, self.username)


class DBCommands:

    async def get_user(self, user_id):
        user = await User.query.where(User.user_id == user_id).gino.first()
        return user

    async def add_new_user(self):
        user = types.User.get_current()
        old_user = await self.get_user(user.id)
        if old_user:
            return old_user
        new_user = User()
        new_user.user_id = user.id
        new_user.username = user.username
        new_user.full_name = user.full_name
        new_user.time = datetime.datetime.now()
        await new_user.create()
        return new_user

    async def count_users(self) -> int:
        total = await db.func.count(User.id).gino.scalar()
        return total

    async def select_all_users(self):
        users = await User.query.gino.all()
        return users


async def create_db():
    await db.set_bind(f'postgresql://{db_user}:{db_pass}@{host}/{db_name}')

    # Create tables
    db.gino: GinoSchemaVisitor
    # await db.gino.drop_all()
    await db.gino.create_all()


def register_models() -> None:
    # todo: register models
    pass
