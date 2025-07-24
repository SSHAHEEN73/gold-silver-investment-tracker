from extensions import db

class Investment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    metal_type = db.Column(db.String(50), nullable=False)

class MetalPrice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    metal_type = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

class ProfitScenario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    scenario_name = db.Column(db.String(100), nullable=False)
    expected_profit = db.Column(db.Float, nullable=False)
