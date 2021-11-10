from flask import request, redirect, render_template
from application import app, db
from application.forms import AddFan, UpdateFan
from application.models import fan, club

@app.route('/')
def home():
    fans = fan.query.all()
    return render_template('Homepage.html', records=fans)