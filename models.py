from extensions import db

class Investment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    metal_type = db.Column(db.String(10), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    purchase_price = db.Column(db.Float, nullable=False)

class MetalPrice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gold = db.Column(db.Float, nullable=False)
    silver = db.Column(db.Float, nullable=False)
