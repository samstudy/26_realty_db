import argparse
import sys
import os
import json
from app_db_init import app, db
from db_model import Flats


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
    for ap in apartments:
        room = Flats(ap['id'], ap['has_balcony'], ap['oblast_district'], 
                     ap['construction_year'], ap['description'], ap['settlement'],
                     ap['rooms_number'],ap['living_area'], ap['address'], ap['price'],
                     ap['premise_area'],ap['under_construction'], ap['is_expired'])
        db.session.add(room)
        db.session.commit()


if __name__ == '__main__':
    file_source = get_args()
    handled_inf = load_data(file_source.source_path)
    insert_into_db_data(handled_inf)