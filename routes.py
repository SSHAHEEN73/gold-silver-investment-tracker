from flask import Blueprint, render_template, request, redirect, url_for, flash
from extensions import db
from models import Investment, MetalPrice

# إنشاء Blueprint
main_bp = Blueprint('main', __name__)

# صفحة Dashboard
@main_bp.route('/dashboard')
def dashboard():
    investments = Investment.query.all()
    prices = MetalPrice.query.order_by(MetalPrice.id.desc()).first()  # آخر سعر مضاف
    return render_template('dashboard.html', investments=investments, prices=prices)

# تحديث أسعار المعادن
@main_bp.route('/update-prices', methods=['GET', 'POST'])
def update_prices():
    if request.method == 'POST':
        gold_price = request.form.get('gold_price')
        silver_price = request.form.get('silver_price')

        if gold_price and silver_price:
            try:
                new_prices = MetalPrice(gold=float(gold_price), silver=float(silver_price))
                db.session.add(new_prices)
                db.session.commit()
                flash("تم تحديث الأسعار بنجاح!", "success")
            except Exception as e:
                flash("حدث خطأ أثناء تحديث الأسعار.", "danger")
        else:
            flash("الرجاء إدخال أسعار الذهب والفضة.", "warning")

        return redirect(url_for('main.dashboard'))

    return render_template('update_prices.html')

# إضافة استثمار جديد
@main_bp.route('/add-investment', methods=['POST'])
def add_investment():
    metal_type = request.form.get('metal_type')
    amount = request.form.get('amount')
    purchase_price = request.form.get('purchase_price')

    if metal_type and amount and purchase_price:
        try:
            new_investment = Investment(
                metal_type=metal_type,
                amount=float(amount),
                purchase_price=float(purchase_price)
            )
            db.session.add(new_investment)
            db.session.commit()
            flash("تمت إضافة الاستثمار بنجاح!", "success")
        except Exception as e:
            flash("حدث خطأ أثناء إضافة الاستثمار.", "danger")
    else:
        flash("الرجاء تعبئة جميع الحقول.", "warning")

    return redirect(url_for('main.dashboard'))
