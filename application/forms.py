from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SelectField, SubmitField


class AddFan(FlaskForm):
    fan_name = StringField("Name")
    salary = SelectField("Salary bracket", choices=['£0-15,000','15,001-25,000','£25,001-35000','£35,000-50,000','£50,001+' ])
    location = StringField("Current location")
    league = SelectField('League', choices=['Premier League','Championship', 'League one', 'League two'])
    team = StringField("Team name")
    submit = SubmitField('Add fan details')

class UpdateFan(FlaskForm):
    fan_name = StringField("Name")
    salary = SelectField("Salary bracket", choices=['£0-15,000','15,001-25,000','£25,001-35000','£35,000-50,000','£50,001+' ])
    location = StringField("Current location")
    league = SelectField('League', choices=['Premier League','Championship', 'League one', 'League two'])
    team = StringField("Team name")
    submit = SubmitField('Add fan details')