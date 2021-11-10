from application import db

class fan(db.Model):
    fanNo = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    salary bracket = db.Column(db.String(50))
    Location = db.Column(db.String(50))
    Club = db.Column(db.String(50), db.ForeignKey('club.clubname')
    League = db.Column(db.String(50))

class club(db.Model):
    clubno = db.Column(db.Integer, primary_key = True)
    clubname = db.Column(db.String(50), primary_key = True)
    league = db.Column(db.String(50))
    fans = db.relationship('fan', backref='supports')