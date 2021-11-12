from application import db

class fan(db.Model):
    fanno = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    salary = db.Column(db.String(50))
    location = db.Column(db.String(50))
    club = db.Column(db.String(50))#, db.ForeignKey('club.clubname')
    league = db.Column(db.String(50))
    club_id = db.Column(db.Integer, db.ForeignKey('club.clubno'))
    

class club(db.Model):
    clubno = db.Column(db.Integer, primary_key = True)
    clubname = db.Column(db.String(50))
    league = db.Column(db.String(50))
    fans = db.relationship('fan', backref='supports')