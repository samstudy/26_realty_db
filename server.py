from flask import Flask, render_template, session, redirect, url_for, escape, request
from app_db_init import app
from db_model import Flats


@app.route("/", methods=['GET'])
def ads_list(page=1):
    post_per_page = 10
    ads = Flats.query.filter(Flats.is_expired == False)
    oblast_district = request.args.get('oblast_district', default=None, type=None)
    min_price = request.args.get('min_price', default=None, type=None)
    max_price = request.args.get('max_price', default=None, type=None)
    under_construction = request.args.get('new_building', True, type=bool)
    if oblast_district:
        ads = ads.filter(Flats.oblast_district == oblast_district)
    if min_price:
        ads = ads.filter(Flats.price > min_price)
    if max_price:
        ads = ads.filter(Flats.price < max_price)
    if under_construction:
        ads = ads.filter(Flats.under_construction == under_construction)
    return render_template('ads_list.html',
                            ads=ads.paginate(page, post_per_page, False),
                            min_price = min_price,
                            max_price= max_price,
                            oblast_district = oblast_district)

if __name__ == "__main__":
    app.run(host='0.0.0.0')