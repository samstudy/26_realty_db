from flask import Flask, render_template, session, redirect, url_for, escape, request
from app_db_init import app
from db_model import Flats



@app.route("/")
def ads_list(page=1):
    post_per_page = 10
    ads = Flats.query.filter(Flats.is_expired==False).paginate(page, post_per_page, False)
    return render_template('ads_list.html', ads=ads)


@app.route('/search', methods=['POST'])
def search(page=1):
    session['dist'] = request.form['oblast_district']
    session['minv'] = request.form['min_price'] 
    session['maxv'] = request.form['max_price']
    session['new_building'] = request.args.get('new_building', True, type=bool)
    return redirect(url_for('results'))


@app.route('/results', methods=['GET'])
def results(page=1):
    post_per_page = 10
    ads = Flats.query.filter(Flats.oblast_district == session['dist'],Flats.is_expired == False, 
          Flats.price > session['minv'], Flats.price < session['maxv'],
          Flats.under_construction == session['new_building']).paginate(page, post_per_page, False)

    return render_template('ads_list.html', ads=ads)


if __name__ == "__main__":
    app.run()