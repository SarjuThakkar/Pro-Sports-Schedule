from app import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    league = db.Column(db.String(12))
    home_team = db.Column(db.String(50))
    away_team = db.Column(db.String(50))
    date = db.Column(db.String(10))
    time = db.Column(db.Integer)
    tv = db.Column(db.String(12))
    timeString = db.Column(db.String(12))

    def __repr__(self):
        return '{}'.format(self.id)


