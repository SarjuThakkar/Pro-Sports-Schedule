import datetime
import csv
from app import db
from app.models import Game

#Edit with file name
with open('NBA.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        date = row[0]
        timeInt = row[1]
        timeStringObj = datetime.time(hour=int(timeInt[0:2]), minute=int(timeInt[2:4]))
        timeString = timeStringObj.strftime("%-I:%M %p")
        tv = row[2]
        away = row[3]
        home = row[4]
        game=Game(date=date, time=timeInt, timeString=timeString, tv=tv, away_team=away, home_team=home, league='NBA');
        db.session.add(game)
    db.session.commit()
