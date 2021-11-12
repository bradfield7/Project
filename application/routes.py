from flask import request, redirect, render_template
from application import app, db
from application.forms import AddFan, UpdateFan, AddClub, UpdateClub
from application.models import fan, club

#@app.route('/')
#def home():
 #   fans = fan.query.all()
#    return render_template('Homepage.html', records=fans)

@app.route('/')
def home():
    return render_template('Homepage.html')

@app.route('/fanlist')
def fanlist():
    fans = fan.query.all()
    return render_template('fanlist.html', records=fans)

@app.route('/clublist')
def clublist():
    clubs = club.query.all()
    return render_template('clublist.html', records=clubs)

@app.route('/editfanRecord/<int:fanno>', methods=['GET', 'POST'])
def editfanForm(fanno):
    form = UpdateFan()
    fan1 = fan.query.filter_by(fanno=fanno).first()
    if request.method == 'POST':
        fan1.name = form.fan_name.data
        fan1.salary = form.salary.data
        fan1.location = form.location.data
        fan1.club = form.club.data
        fan1.league = form.league.data
        fan1.club_id = form.club_id.data
        db.session.commit()
        return redirect("/fanlist")
    return render_template('faneditform.html', form=form)

@app.route('/editclubRecord/<int:clubno>', methods=['GET', 'POST'])
def editclubForm(clubno):
    form = UpdateClub()
    club1 = club.query.filter_by(clubno=clubno).first()
    if request.method == 'POST':
        club1.league = form.league.data
        club1.clubname = form.club.data
        
        db.session.commit()
        return redirect("/clublist")
    return render_template('clubeditform.html', form=form)


@app.route("/savefanRecord",methods=["GET","POST"])
def savefanRecord():
    form = AddFan()
    if request.method == 'POST':
        name=form.fan_name.data
        salary=form.salary.data
        location=form.location.data
        club = form.club.data
        league = form.league.data
        club_id = form.club_id.data
        newfan = fan(name=name, salary=salary, location=location, club=club, league=league, club_id=club_id)
        db.session.add(newfan)
        db.session.commit()
        return redirect("/")
    return render_template("faninputform.html", form=form)

@app.route("/saveclubRecord",methods=["GET","POST"])
def saveclubRecord():
    form = AddClub()
    if request.method == 'POST':
        league = form.league.data
        club1 = form.club.data
        newclub = club(clubname=club1,league=league )
        db.session.add(newclub)
        db.session.commit()
        return redirect("/")
    return render_template("clubinputform.html", form=form)

@app.route("/fandetails/<int:fanno>")
def fanInformation(fanno):
	data = fan.query.filter_by(fanno=fanno).first()
	return render_template("faninformation.html",record=data)

@app.route("/clubdetails/<int:clubno>")
def clubInformation(clubno):
	data = club.query.filter_by(clubno=clubno).first()
	return render_template("clubinformation.html",record=data)

@app.route("/deleteFan/<int:fanno>")
def deleteFan(fanno):
    fan1 = fan.query.filter_by(fanno=fanno).first()
    db.session.delete(fan1)
    db.session.commit()
    return redirect("/")

@app.route("/deleteClub/<int:clubno>")
def deleteClub(clubno):
    club1 = club.query.filter_by(clubno=clubno).first()
    db.session.delete(club1)
    db.session.commit()
    return redirect("/")