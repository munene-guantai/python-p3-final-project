from sqlalchemy import Column, Integer, String, Float, DateTime

from mullawatch import db

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True)
    email = Column(String(255), unique=True)
    password = Column(String(255))

class Account(db.Model):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, db.ForeignKey('users.id'))
    name = Column(String(255))
    type = Column(String(255))
    balance = Column(Float)

class Category(db.Model):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    parent_id = Column(Integer, db.ForeignKey('categories.id'))

class Transaction(db.Model):
    __tablename__ = 'categoeries'

    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, db.ForeignKey('accounts.id'))
    category_id = Column(Integer, db.ForeignKey('categories.id'))
    amount = Column(Float)
    date = Column(DateTime)