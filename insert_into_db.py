import argparse
import sys
import os
import json
from app_db_init import app, db
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
        flat_for_update = Flats.query.filter_by(room_id = apartment['id']).first()
        if flat_for_update:
            flat_for_update.has_balcony = apartment['has_balcony'],
            flat_for_update.oblast_district = apartment['oblast_district'],
            flat_for_update.construction_year = apartment['construction_year'],
            flat_for_update.description = apartment['description'],
            flat_for_update.settlement = apartment['settlement'],
            flat_for_update.rooms_number = apartment['rooms_number'],
            flat_for_update.living_area = apartment['living_area'],
            flat_for_update.address = apartment['address'],
            flat_for_update.price = apartment['price'],
            flat_for_update.premise_area = apartment['premise_area'],
            flat_for_update.under_construction = apartment['under_construction']
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

def hide_irrelevant_flats(apartments):
    actual_flats = [apartment['id'] for apartment in apartments]
    all_flats = Flats.query.order_by(Flats.room_id).all()
    for flat in all_flats:
        if flat.room_id not in actual_flats:
            flat.is_expired = True
            db.session.commit()


if __name__ == '__main__':
    file_source = get_args()
    handled_inf = load_data(file_source.source_path)
    insert_into_db_data(handled_inf)
    hide_irrelevant_flats(handled_inf)