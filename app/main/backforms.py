from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, SelectField, SelectMultipleField
from wtforms.validators import ValidationError, DataRequired, Length
from flask_babel import _, lazy_gettext as _l


class EditProfileForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    about_me = TextAreaField(_l('About me'),
                             validators=[Length(min=0, max=140)])
    submit = SubmitField(_l('Submit'))

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError(_('Please use a different username.'))


class PostForm(FlaskForm):
    post = TextAreaField(_l('Say something'), validators=[DataRequired()])
    submit = SubmitField(_l('Submit'))


class CrudForm(FlaskForm):
    title = StringField(_l('Title'), validators=[DataRequired()])
    description = TextAreaField(_l('Description'))
    tiny_description = TextAreaField(_l('Tiny Description'))
    short_description = TextAreaField(_l('Short Description'))
    medium_description = TextAreaField(_l('Medium Description'))
    long_description = TextAreaField(_l('Long Description'))
    price = StringField(_l('Price'), validators=[DataRequired()])
    shelf_time = StringField(_l('Shelf Time'), validators=[DataRequired()])
    campus_id = StringField(_l('Campus ID'), validators=[DataRequired()])
    last_update = StringField(_l('Last Update'))
    archived = BooleanField(_l('Archived'))
    taxable = BooleanField(_l('Taxable'))
    category_names = StringField(_l('Category Names'))
    vendor = StringField(_l('Campus ID'), validators=[DataRequired()])
    source = StringField(_l('Source'), validators=[DataRequired()])
    notes = TextAreaField(_l('Notes'))
    total_cal = StringField(_l('Total Calories'), validators=[DataRequired()])
    num_servings = StringField(_l('Num Servings'), validators=[DataRequired()])
    ingredients = TextAreaField(_l('Ingredients'))
    calories = StringField(_l('Calories'), validators=[DataRequired()])
    proteins = StringField(_l('Proteins'), validators=[DataRequired()])
    sugar = StringField(_l('Sugar'), validators=[DataRequired()])
    carbohydrates = StringField(_l('Carbohydrates'), validators=[DataRequired()])
    fat = StringField(_l('Fat'), validators=[DataRequired()])
    consumer_category = StringField(_l('Consumer Category'), validators=[DataRequired()])
    ws_case_size = StringField(_l('Case Size'), validators=[DataRequired()])
    kiosk_ship_qty = StringField(_l('Kiosk Ship Qty'), validators=[DataRequired()])
    pick_station = StringField(_l('Pick Station'), validators=[DataRequired()])
    fc_title = StringField(_l('FC Title'))
    width_space = StringField(_l('Width Space'), validators=[DataRequired()])
    height_space = StringField(_l('Height Space'), validators=[DataRequired()])
    depth_space = StringField(_l('Depth Space'), validators=[DataRequired()])
    slotted_width = StringField(_l('Slotted Station'), validators=[DataRequired()])
    tag_volume = StringField(_l('Tag Volume'), validators=[DataRequired()])
    delivery_option = StringField(_l('Tag Volume'), validators=[DataRequired()])
    tag_applied_by = StringField(_l('Tag Applied'))
    submit = SubmitField(_l('Submit'))


