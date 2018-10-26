from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import ValidationError, DataRequired, Length
from flask_babel import _, lazy_gettext as _l


class CrudForm(FlaskForm):

    id = StringField('id', validators=[DataRequired()], render_kw={'readonly': True})
    title = StringField(_l('Title'), validators=[DataRequired()])
    description = TextAreaField(_l('Description'))
    tiny_description = TextAreaField(_l('Tiny Description'))
    short_description = TextAreaField(_l('Short Description'))
    medium_description = TextAreaField(_l('Medium Description'))
    long_description = TextAreaField(_l('Long Description'))
    price = StringField(_l('Price'), validators=[DataRequired()])
    shelf_time = StringField(_l('Shelf Time'),  validators=[DataRequired()])
    campus_id = StringField(_l('Campus ID'), validators=[DataRequired()])
    last_update = StringField(_l('Last Update'))
    archived = BooleanField(_l('Archived'))
    taxable = BooleanField(_l('Taxable'), validators=[DataRequired()])
    category_names = StringField(_l('Category Names'))
    vendor = StringField(_l('Campus ID'))
    source = StringField(_l('Source'))
    notes = TextAreaField(_l('Notes'))
    total_cal = StringField(_l('Total Calories'))
    num_servings = StringField(_l('Num Servings'))
    ingredients = TextAreaField(_l('Ingredients'))
    calories = StringField(_l('Calories'))
    proteins = StringField(_l('Proteins'))
    sugar = StringField(_l('Sugar'))
    carbohydrates = StringField(_l('Carbohydrates'))
    fat = StringField(_l('Fat'))
    consumer_category = StringField(_l('Consumer Category'))
    ws_case_size = StringField(_l('Case Size'))
    kiosk_ship_qty = StringField(_l('Kiosk Ship Qty'))
    pick_station = StringField(_l('Pick Station'))
    fc_title = StringField(_l('FC Title'))
    width_space = StringField(_l('Width Space'), validators=[DataRequired()])
    height_space = StringField(_l('Height Space'), validators=[DataRequired()])
    depth_space = StringField(_l('Depth Space'), validators=[DataRequired()])
    slotted_width = StringField(_l('Slotted Width'), validators=[DataRequired()])
    tag_volume = StringField(_l('Tag Volume'), validators=[DataRequired()])
    delivery_option = StringField(_l('Delivery Volume'), validators=[DataRequired()])
    tag_applied_by = StringField(_l('Tag Applied'))
    submit = SubmitField(_l('Submit'))


