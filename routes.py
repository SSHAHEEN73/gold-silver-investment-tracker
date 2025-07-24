from flask import Blueprint, render_template, request, redirect, url_for
from extensions import db
from models import Investment, MetalPrice, ProfitScenario

# إنشاء Blueprint
main_bp = Blueprint('main', __name__)

# الصفحة الرئيسية أو أي صفحة تريدها
@main_bp.route('/')
def index():
    investments = Investment.query.all()
    prices = MetalPrice.query.all()
    return render_template('index.html', investments=investments, prices=prices)

# مثال على تحديث أسعار المعادن
@main_bp.route('/update', methods=['GET', 'POST'])
def update_prices():
    if request.method == 'POST':
        gold_price = request.form.get('gold_price')
        silver_price = request.form.get('silver_price')

        if gold_price and silver_price:
            new_prices = MetalPrice(gold=float(gold_price), silver=float(silver_price))
            db.session.add(new_prices)
            db.session.commit()
            return redirect(url_for('main.index'))

    return render_template('update.html')

# مثال على إضافة استثمار
@main_bp.route('/add-investment', methods=['POST'])
def add_investment():
    metal_type = request.form.get('metal_type')
    amount = request.form.get('amount')
    purchase_price = request.form.get('purchase_price')

    if metal_type and amount and purchase_price:
        new_investment = Investment(
            metal_type=metal_type,
            amount=float(amount),
            purchase_price=float(purchase_price)
        )
        db.session.add(new_investment)
        db.session.commit()

    return redirect(url_for('main.index'))
