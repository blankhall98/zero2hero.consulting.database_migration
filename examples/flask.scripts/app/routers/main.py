from flask import blueprints, render_template, request, redirect, url_for, flash
from app.scripts.code import Manager

main = blueprints.Blueprint('main', __name__)

@main.route('/')
def index():
    return 'Index Page'

@main.route('/calculate/CI', methods=['GET','POST'])
def calculate_CI():
    if request.method == 'POST':
        initial_investment = request.form['InitialInvestment']
        rate_of_return = request.form['RateOfReturn']
        years = request.form['Time']
        manager = Manager()
        result = manager.calculate_CI(float(initial_investment),float(rate_of_return),float(years))
        return str(result)
    else:
        return render_template('CI.html')
    
