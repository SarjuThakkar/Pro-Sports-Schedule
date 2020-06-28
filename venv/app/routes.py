from flask import render_template, request
from app import app, db
from app.models import Game
from datetime import date

@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
        currDate = date.today()
        games = Game.query.filter(Game.date == currDate).all()
        games.sort(key=time)
        leagues = [r.league for r in db.session.query(Game.league).distinct()]
        leaguesChecked = {}
        for league in leagues:
                leaguesChecked[league] = 'checked'
        tvsChecked = {}
        tvs = [r.tv for r in db.session.query(Game.tv).distinct()]
        for tv in tvs:
                tvsChecked[tv] = 'checked'
        if request.method == 'POST':
                leaguesChosen = request.form.getlist('leagueCheckbox')
                for league in leagues:
                        if league in leaguesChosen:
                                leaguesChecked[league] = 'checked'
                        else:
                                leaguesChecked[league] = ''
                tvsChosen = request.form.getlist('tvCheckbox')
                for tv in tvs:
                        if tv in tvsChosen:
                                tvsChecked[tv] = 'checked'
                        else:
                                tvsChecked[tv] = ''
                currDate = request.form.get('datePicker')
                games = Game.query.filter(Game.date == currDate).filter((Game.league.in_(leaguesChosen))).filter(Game.tv.in_(tvsChosen)).all()
                games.sort(key=time)
        return render_template('index.html', title='Home', games=games, leagues=leagues, tvs=tvs, currDate=currDate, leaguesChecked=leaguesChecked, tvsChecked=tvsChecked)
