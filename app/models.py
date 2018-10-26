from datetime import datetime
from app import db



class Product(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(120), index=True)
    description = db.Column(db.String(400))
    tiny_description = db.Column(db.String(200))
    short_description = db.Column(db.String(200))
    medium_description = db.Column(db.String(200))
    long_description = db.Column(db.String(200))
    price = db.Column(db.String(200))
    shelf_time = db.Column(db.String(200))
    campus_id = db.Column(db.String(200))
    # TODO look into why SQLite hates DATETIME
    last_update = db.Column(db.Integer)
    archived = db.Column(db.Boolean)
    taxable = db.Column(db.Boolean)
    category_names = db.Column(db.String(200))
    vendor = db.Column(db.String(200))
    source = db.Column(db.String(50))
    notes = db.Column(db.String(200))
    total_cal = db.Column(db.Integer)
    num_servings = db.Column(db.Integer)
    ingredients = db.Column(db.String(200))
    calories = db.Column(db.Integer)
    proteins = db.Column(db.Integer)
    sugar = db.Column(db.Integer)
    carbohydrates = db.Column(db.Integer)
    fat = db.Column(db.Integer)
    consumer_category = db.Column(db.String(50))
    ws_case_size = db.Column(db.Integer)
    kiosk_ship_qty = db.Column(db.Integer)
    pick_station = db.Column(db.Integer)
    fc_title = db.Column(db.String(100))
    width_space = db.Column(db.Integer)
    height_space = db.Column(db.Integer)
    depth_space = db.Column(db.Integer)
    slotted_width = db.Column(db.Integer)
    tag_volume = db.Column(db.Integer)
    delivery_option = db.Column(db.Integer)
    tag_applied_by = db.Column(db.String(2))

    def save_product(self, form, new=False):

        self.title = form.title.data
        self.description = form.description.data
        self.tiny_description = form.tiny_description.data
        self.short_description = form.short_description.data
        self.medium_description = form.medium_description.data
        self.long_description = form.long_description.data
        self.price = form.price.data
        self.shelf_time = form.shelf_time.data
        self.campus_id = form.campus_id.data
        self.last_update = datetime.now()
        self.archived = form.archived.data
        self.taxable = form.taxable.data
        self.category_names = form.category_names.data
        self.vendor = form.vendor.data
        self.source = form.source.data
        self.notes = form.notes.data
        self.total_cal = form.total_cal.data
        self.num_servings = form.num_servings.data
        self.ingredients = form.ingredients.data
        self.calories = form.calories.data
        self.proteins = form.proteins.data
        self.sugar = form.sugar.data
        self.carbohydrates = form.carbohydrates.data
        self.fat = form.fat.data
        self.consumer_category = form.consumer_category.data
        self.ws_case_size = form.ws_case_size.data
        self.kiosk_ship_qty = form.kiosk_ship_qty.data
        self.pick_station = form.pick_station.data
        self.fc_title = form.fc_title.data
        self.width_space = form.width_space.data
        self.height_space = form.height_space.data
        self.depth_space = form.depth_space.data
        self.slotted_width = form.slotted_width.data
        self.tag_volume = form.tag_volume.data
        self.delivery_option = form.delivery_option.data
        self.tag_applied_by = form.tag_applied_by.data

        if new:
            # Add the product to the database
            db.session.add(self)
            # commit the data to the database

        db.session.commit()



    def delete_product(self):
        db.session.remove()
        db.session.commit()

    def __repr__(self):
        return '<Product %r>' % (self.title)

