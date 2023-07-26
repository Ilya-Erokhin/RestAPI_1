from db import db

# Inherits from db.Model
class ItemModel(db.Model):
# __tablename__ is gonna tells SQLALCHEMY what the table name is gonna be when created
    __tablename__ = 'items'

# Columns we are going to store in our Table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80)) # 80 - max characters
    price = db.Column(db.Float(precision=2)) # With 2 elements of precision, after decimal point

# __init__ method the let us give the item, a name and a price
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Json method returns a dictionary, representing this Item
    def json(self):
        return {'name': self.name, 'price': self.price}

# @classmethod - Finds item by name
# cls - refers to the class (cls == ItemModel)
# and get the First Item
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

# Adding and Deleting the Item to the current session
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
