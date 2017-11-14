import argparse
import sys
import os
import json
from ap_db_init import app, db
from db_model import Flats
from sqlalchemy import update


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('source_path', help='Mandatory parametr')
    return parser.parse_args()


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def insert_into_db_data(apartments):
    for apartment in apartments:
        updated_flats = Flats.query.filter_by(room_id = apartment['id']).first()
        if updated_flats:
            updated_flats.has_balcony = apartment['has_balcony'],
            updated_flats.oblast_district = apartment['oblast_district'],
            updated_flats.construction_year = apartment['construction_year'],
            updated_flats.description = apartment['description'],
            updated_flats.settlement = apartment['settlement'],
            updated_flats.rooms_number = apartment['rooms_number'],
            updated_flats.living_area = apartment['living_area'],
            updated_flats.address = apartment['address'],
            updated_flats.price = apartment['price'],
            updated_flats.premise_area = apartment['premise_area'],
            updated_flats.under_construction = apartment['under_construction']
            db.session.commit()
        else:

            room = Flats(apartment['id'], apartment['has_balcony'],
                         apartment['oblast_district'],apartment['construction_year'],
                         apartment['description'], apartment['settlement'],
                         apartment['rooms_number'],apartment['living_area'],
                         apartment['address'], apartment['price'],apartment['premise_area'],
                         apartment['under_construction'],apartment['is_expired'])
            db.session.add(room)
            db.session.commit()


if __name__ == '__main__':
    file_source = get_args()
    handled_inf = load_data(file_source.source_path)
    insert_into_db_data(handled_inf)