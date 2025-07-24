from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class InvestmentForm(FlaskForm):
    date = DateField('Date', validators=[DataRequired()])
    metal_type = SelectField('Metal Type', choices=[('gold', 'Gold'), ('silver', 'Silver')])
    investment_amount = FloatField('Investment Amount', validators=[DataRequired()])
    currency = SelectField('Currency', choices=[('AED', 'AED'), ('KWD', 'KWD')])
    price_per_gram = FloatField('Price per Gram', validators=[DataRequired()])
    submit = SubmitField('Add Investment')

class PriceUpdateForm(FlaskForm):
    metal_type = SelectField('Metal Type', choices=[('gold', 'Gold'), ('silver', 'Silver')])
    price_aed = FloatField('Price (AED)', validators=[DataRequired()])
    submit = SubmitField('Update Price')

class ProfitCalculatorForm(FlaskForm):
    name = StringField('Scenario Name', validators=[DataRequired()])
    percentage_growth = FloatField('Growth %', validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField('Add Scenario')
