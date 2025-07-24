from app import db
from datetime import datetime

class Investment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    metal_type = db.Column(db.String(10), nullable=False)  # gold or silver
    investment_amount = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(5), nullable=False)  # AED or KWD
    price_per_gram = db.Column(db.Float, nullable=False)
    quantity_grams = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Investment {self.metal_type} {self.investment_amount} {self.currency}>'

class MetalPrice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    metal_type = db.Column(db.String(10), nullable=False)
    price_aed = db.Column(db.Float, nullable=False)  # Price per gram in AED
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<MetalPrice {self.metal_type} {self.price_aed} AED/gram>'

class ProfitScenario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    percentage_growth = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<ProfitScenario {self.name} {self.percentage_growth}%>'
