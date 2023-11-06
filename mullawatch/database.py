import sqlalchemy as sa

from mullawatch import app

db = sa.create_engine(app.config['SQLALCHEMY_DATABASE_'])