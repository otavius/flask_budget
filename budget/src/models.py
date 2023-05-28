from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.inspection import inspect

db = SQLAlchemy()


# class Serializer(object):

#     def serialize(self):
#         return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

#     @staticmethod
#     def serialize_list(l):
#         return [m.serialize() for m in l]


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128), nullable=False)
    username = db.Column(db.String(128), unique=True, nullable=False)

    def __init__(self, first_name: str, last_name: str, email: str, password: str, username: str):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.username = username

    def serialize(self):
        # d = Serializer.serialize(self)
        # return d
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'password': self.password,
            'username': self.username,
        }
        
    def insert(self):
        db.session.add(self)
        db.session.commit()


class Expense(db.Model):
    __tablename__ = 'expenses'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    expense_name = db.Column(db.String(128), nullable=False)
    expense_amount = db.Column(db.Float, nullable=False, default=0.)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    category = db.Column(db.String(50), nullable=True)

    def __init__(self, expense_name: str, expense_amount: int, user_id: int, category: str):
        self.expense_name = expense_name
        self.expense_amount = expense_amount
        self.user_id = user_id

    def serialize(self):
        return {
            'id': self.id,
            'expense_name': self.expense_name,
            'expense_amount': self.expense_amount,
            'user_id': self.user_id,
            'category': self.category

        }

    def insert(self):
        db.session.add(self)
        db.session.commit()