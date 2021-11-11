from flask import request, redirect, render_template
from application import app, db
from application.forms import AddFan, UpdateFan, AddClub, UpdateClub
from application.models import fan, club

@app.route('/')
def home():
    fans = fan.query.all()
    return render_template('Homepage.html', records=fans)

@app.route('/editfanRecord/<int:fanno>', methods=['GET', 'POST'])
def editRecordForm(fanno):
    form = UpdateFan()
    fan = fan.query.filter_by(fanno=fanno).first()
    if request.method == 'POST':
        fan.name = form.fan_name.data
        fan.salary = form.salary.data
        fan.location = form.location.data
        fan.club = form.club.data
        fan.league = form.league.data
        db.session.commit()
        return redirect("/")
    return render_template('faneditform.html', form=form)

@app.route('/editclubRecord/<int:clubno>', methods=['GET', 'POST'])
def editRecordForm(fanno):
    form = UpdateClub()
    club = club.query.filter_by(clubno=clubno).first()
    if request.method == 'POST':
        club.league = form.league.data
        club.club = form.club.data
        
        db.session.commit()
        return redirect("/")
    return render_template('clubeditform.html', form=form)


@app.route("/savefanRecord",methods=["GET","POST"])
def saveRecord():
    form = AddFan()
    if request.method == 'POST':
        name=form.fan_name.data
        salary=form.salary.data
        location=form.location.data
        club = form.club.data
        league = form.league.data
        newfan = fan(name=name, salary=salary, location=location, club=club, league=league)
        db.session.add(newfan)
        db.session.commit()
        return redirect("/")
    return render_template("faninputform.html", form=form)

@app.route("/saveclubRecord",methods=["GET","POST"])
def saveRecord():
    form = AddClub()
    if request.method == 'POST':
        league = form.league.data
        club = form.club.data
        newclub = club(league=league, club=club)
        db.session.add(newclub)
        db.session.commit()
        return redirect("/")
    return render_template("clubinputform.html", form=form)

@app.route("/fandetails/<int:fanno>")
def fanInformation(fanno):
	data = fan.query.filter_by(fanno=fanno).first()
	return render_template("faninformation.html",record=data)

@app.route("/clubdetails/<int:clubno>")
def clubInformation(fanno):
	data = club.query.filter_by(clubno=clubno).first()
	return render_template("clubinformation.html",record=data)

@app.route("/deleteFan/<int:fanno>")
def deleteFan(fanno):
    fan = fan.query.filter_by(fanno=fanno).first()
    db.session.delete(fan)
    db.session.commit()
    return redirect("/")

@app.route("/deleteClub/<int:clubno>")
def deleteClub(clubno):
    fan = club.query.filter_by(clubno=clubno).first()
    db.session.delete(club)
    db.session.commit()
    return redirect("/")