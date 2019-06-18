from flask_bcrypt import bcrypt
from flask_login import UserMixin
from peewee import *

DATABASE = SqliteDatabase('tacocat.db')


class User(UserMixin, Model):
    email = CharField(unique=True)
    password = CharField(max_length=100)

    class Meta:
        database = DATABASE

    @classmethod
    def create_user(cls, email, password):
        try:
            cls.create(
                email=email,
                password=generate_password_hash(password)
            )
        except IntegrityError:
            raise ValueError("User already exists")


class Taco(Model):
    user = ForeignKeyField(
        rel_model=User,
        related_name='tacos'
    )
    protein = CharField()
    shell = CharField()
    cheese = BooleanField()
    extras = TextField(default='')

    class Meta:
        database = DATABASE
