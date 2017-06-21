from app_db_init import app, db


class Flats(db.Model):
    __tablename__='ASSETS'
    room_id = db.Column(db.Integer, primary_key=True)
    has_balcony = db.Column(db.Boolean)
    oblast_district = db.Column(db.Text(120))
    construction_year = db.Column(db.Integer)
    description = db.Column(db.Text(1000))
    settlement = db.Column(db.Text(100))
    rooms_number = db.Column(db.Integer)
    living_area = db.Column(db.Float)
    address = db.Column(db.Text(100))
    price = db.Column(db.Integer)
    premise_area = db.Column(db.Float)
    under_construction = db.Column(db.Boolean)
    is_expired = db.Column(db.Boolean)


    def __init__(self, room_id, has_balcony, oblast_district, construction_year,
                  description, settlement, rooms_number, living_area,
                  address, price, premise_area, under_construction, is_expired):
        self.id = room_id
        self.has_balcony = has_balcony
        self.oblast_district = oblast_district
        self.construction_year = construction_year
        self.description = description
        self.settlement = settlement
        self.rooms_number = rooms_number
        self.living_area = living_area
        self.address = address
        self.price = price
        self.premise_area = premise_area
        self.under_construction = under_construction
        self.is_expired = is_expired