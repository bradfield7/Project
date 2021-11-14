from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import fan, club
import application.routes
from application.forms import AddFan, AddClub, UpdateFan, UpdateClub
import pytest
from os import getenv

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            SECRET_KEY='TEST_SECRET_KEY',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app
    def setUp(self):
        db.create_all()
        sample1 = club(clubname='Sunderland', league='League one')
        db.session.add(sample1)
        db.session.commit()
        sample = fan(name='John', salary='£0-15,000', location='Doncaster', club='Sunderland', league='League one', club_id=1)
        db.session.add(sample)
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestViews(TestBase):
    def test_fans_get(self):
        response = self.client.get(url_for('fanlist'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'John', response.data)
    
    def test_clubs_get(self):
        response = self.client.get(url_for('clublist'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Sunderland', response.data)

    def test_add_fan(self):
        response = self.client.post(
            url_for('savefanRecord'),
            data = dict(fan_name='Brad', salary='£0-15,000', location='Doncaster', club='Sunderland', league='League one', club_id=1),
            follow_redirects = True
        )
        self.assertIn(b'Brad', response.data)

    def test_add_club(self):
        response = self.client.post(
            url_for('saveclubRecord'),
            data = dict(league='League one', club='Doncaster Rovers'),
            follow_redirects = True
        )
        self.assertIn(b'Doncaster Rovers', response.data)

   
    
    def test_update_fan(self):
        response = self.client.post(
            url_for('editfanForm', fanno=1),
            data = dict(fan_name='Johnny', salary='£0-15,000', location='Doncaster', club='Sunderland', league='League one', club_id=1),
            follow_redirects = True
        )
        self.assertIn(b'Johnny', response.data)

    def test_update_club(self):
        response = self.client.post(
            url_for('editclubForm', clubno=1),
            data = dict(league='League one', club='Doncaster Rovers'),
            follow_redirects = True
        )
        self.assertIn(b'Doncaster Rovers', response.data)

    
    def test_fan_info(self):
        response = self.client.get(url_for('fanInformation', fanno=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'John', response.data)

    def test_club_info(self):
        response = self.client.get(url_for('clubInformation', clubno=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Sunderland', response.data)
    
    def test_del_fan(self):
        response = self.client.get(url_for('deleteFan', fanno=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Fanbase Colleration Survey', response.data)

    def test_del_club(self):
        response = self.client.get(url_for('deleteClub', clubno=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Fanbase Colleration Survey', response.data)
    
    def test_view_fanedit(self):
        response = self.client.get(url_for('editfanForm', fanno=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'fan_name', response.data)
    
    def test_view_clubedit(self):
        response = self.client.get(url_for('editclubForm', clubno=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'league', response.data)
    
    def test_view_fanadd(self):
        response = self.client.get(url_for('savefanRecord'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'fan_name', response.data)
    
    def test_view_clubadd(self):
        response = self.client.get(url_for('saveclubRecord'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'league', response.data)
    
