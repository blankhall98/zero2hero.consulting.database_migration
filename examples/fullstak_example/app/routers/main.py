from flask import render_template, blueprints
from app.models.spiders import Spider

main = blueprints.Blueprint('main', __name__)

@main.route('/')
def home():
    spiders = Spider.query.all()
    return render_template('spiders.html', spiders=spiders)