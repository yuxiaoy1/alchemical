from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from alchemical import Alchemical, Model

db = Alchemical('sqlite:///users.sqlite', binds={
    'groups': 'sqlite:///groups.sqlite'
})


class User(Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(128))


class Group(Model):
    __bind_key__ = 'groups'
    __tablename__ = 'groups'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(128))
