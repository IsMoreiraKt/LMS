from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from enum import Enum
from app import database



class UserRole(Enum):
    USER = 'user'
    VENDEDOR = 'vendedor'
    ADMIN = 'admin'



class UserModel(database.Model):
    __tablename__ = 'users'

    id = database.Column(
        database.Integer, 
        primary_key=True
    )
    name = database.Column(
        database.String(75),
        nullable=False
    )
    email = database.Column(
        database.String(115),
        unique=True,
        nullable=False
    )
    password_hash = database.Column(
        database.String(128),
        nullable=False
    )
    role = database.Column(
        database.Enum(UserRole),
        default=UserRole.USER,
        nullable=False
    )

    created_at = database.Column(
        database.DateTime,
        default=datetime.utcnow
    )
    
    updated_at = database.Column(
        database.DateTime, 
        default=datetime.utcnow, 
        onupdate=datetime.utcnow
    )


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)


    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


    def __repr__(self):
        return f'<User {self.email} - {self.role.name}>'