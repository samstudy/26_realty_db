from flask import Flask, render_template, session, redirect, url_for, escape, request
from app_db_init import app
from db_model import Flats



@app.route("/")
def ads_list(page=1):
    ads = Flats.query.filter(Flats.is_expired==False).paginate(page, POSTS_PER_PAGE, False)
    return render_template('ads_list.html', ads=ads)


@app.route('/search', methods=['POST'])
def search(page=1):
    session['dist'] = request.form['oblast_district']
    session['minv'] = request.form['min_price'] 
    session['maxv'] = request.form['max_price']
    return redirect(url_for('results'))


@app.route('/results', methods=['GET'])
def results(page=1):
    ads = Flats.query.filter(Flats.oblast_district == session['dist'],Flats.is_expired == False, 
          Flats.price > session['minv'], Flats.price < session['maxv']).paginate(page, POSTS_PER_PAGE, False)
    return render_template('ads_list.html', ads=ads)


if __name__ == "__main__":
    app.run()