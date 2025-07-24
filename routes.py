from flask import render_template, redirect, url_for, flash, request
from app import app, db
from models import Investment, MetalPrice, ProfitScenario
from forms import InvestmentForm, PriceUpdateForm, ProfitCalculatorForm
from datetime import datetime

@app.route('/')
def index():
    investments = Investment.query.all()
    prices = MetalPrice.query.all()
    scenarios = ProfitScenario.query.all()
    return render_template('index.html', investments=investments, prices=prices, scenarios=scenarios)

@app.route('/add_investment', methods=['GET', 'POST'])
def add_investment():
    form = InvestmentForm()
    if form.validate_on_submit():
        investment_amount = form.investment_amount.data or 0
        price_per_gram = form.price_per_gram.data or 0

        # تحويل إذا العملة KWD
        if form.currency.data == 'KWD':
            investment_amount *= 12
            price_per_gram *= 12

        quantity_grams = (investment_amount / price_per_gram) if price_per_gram > 0 else 0

        new_investment = Investment(
            date=form.date.data,
            metal_type=form.metal_type.data,
            investment_amount=form.investment_amount.data,
            currency=form.currency.data,
            price_per_gram=form.price_per_gram.data,
            quantity_grams=quantity_grams
        )
        db.session.add(new_investment)
        db.session.commit()
        flash('Investment added successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('add_investment.html', form=form)
