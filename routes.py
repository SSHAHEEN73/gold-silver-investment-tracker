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

        # تحويل إذا العملة KWD (ضرب المبلغ فقط)
        if form.currency.data == 'KWD':
            investment_amount *= 12  # تحويل المبلغ إلى AED

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

@app.route('/update_price', methods=['GET', 'POST'])
def update_price():
    form = PriceUpdateForm()
    if form.validate_on_submit():
        metal = MetalPrice.query.filter_by(metal_type=form.metal_type.data).first()
        if not metal:
            metal = MetalPrice(metal_type=form.metal_type.data, price_aed=form.price_aed.data)
            db.session.add(metal)
        else:
            metal.price_aed = form.price_aed.data
            metal.last_updated = datetime.utcnow()
        db.session.commit()
        flash('Price updated successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('update_price.html', form=form)

@app.route('/add_scenario', methods=['GET', 'POST'])
def add_scenario():
    form = ProfitCalculatorForm()
    if form.validate_on_submit():
        new_scenario = ProfitScenario(name=form.name.data, percentage_growth=form.percentage_growth.data)
        db.session.add(new_scenario)
        db.session.commit()
        flash('Scenario added successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('add_scenario.html', form=form)
