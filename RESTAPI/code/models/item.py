from db import db

class ItemModel(db.Model):

    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    price = db.Column(db.Float(precision=2))
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):

        return {"id": self.id, "name": self.name, "price": self.price, "store_id": self.store_id}

    
    def save_to_db(self):

        db.session.add(self)
        db.session.commit()
        

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()      
        

    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def return_all_items(cls):

        return list(map(lambda x : x.json(), cls.query.all()))

