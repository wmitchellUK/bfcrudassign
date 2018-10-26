import csv
from flask import render_template, flash, redirect, url_for, request
from sqlalchemy.exc import IntegrityError

from app import db
from app.main.forms import CrudForm
from app.main.tables import Results
from app.models import Product
from app.main import bp


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    # show new items first
    qry = db.session.query(Product).order_by(Product.id.desc())
    results = qry.all()
    table = Results(results)

    table.border = True
    table.classes = ['table', 'table-striped']
    return render_template('index.html', table=table)


@bp.route('/create_product', methods=['GET', 'POST'])
def create_product():
    form = CrudForm(request.form)

    if request.method == 'POST':
        # save the product
        product = Product()
        product.save_product(form, new=True)
        flash('Product created successfully!')
        return redirect('/')

    return render_template('new_product.html', form=form)


@bp.route('/read_product/<int:id>', methods=['GET', 'POST'])
def read_product(id):
    qry = db.session.query(Product).filter(
        Product.id == id)
    product = qry.first()

    if product:
        form = CrudForm(formdata=request.form, obj=product)
        return render_template('read_product.html', form=form)
    else:
        return 'Error loading #{id}'.format(id=id)


@bp.route('/edit_product/<int:id>', methods=['GET', 'POST'])
def update_product(id):
    qry = db.session.query(Product).filter(
        Product.id == id)
    product = qry.first()

    if product:
        form = CrudForm(formdata=request.form, obj=product)
        if request.method == 'POST':
            product.save_product(form)
            flash('Product updated successfully')
        return render_template('edit_product.html', form=form)
    else:
        flash('Error loading Product')
        return redirect(url_for('main.index'))


@bp.route('/delete_product/item/<int:id>', methods=['GET', 'POST'])
def delete_product(id):
    qry = db.session.query(Product).filter(
        Product.id==id)
    product = qry.first()

    if product and request.method == 'GET':
        db.session.delete(product)
        db.session.commit()

        flash('Product deleted successfully')
        return redirect(url_for('main.index'))
    else:
        return 'Error loading #{id}'.format(id=id)


@bp.route('/import', methods=['GET'])
def import_csv():
    try:
        with open('csv/product_subset_filtered.csv') as f:
            reader = csv.reader(f)
            for count, row in enumerate(reader, start=0):
                if count == 0:
                    print('Skipping headers')
                    continue

                query = Product(id=row[0], title=row[1], description=row[2], tiny_description=row[3], short_description=row[4],
                                medium_description=row[5], long_description=row[6], price=row[7], shelf_time=row[8], campus_id=row[9],
                                last_update=row[10], archived=row[11], taxable=row[12], category_names=row[13], vendor=row[14],
                                source=row[15], notes=row[16], total_cal=row[17], num_servings=row[18], ingredients=row[19],
                                calories=row[20], proteins=row[21], sugar=row[22], carbohydrates=row[23], fat=row[24],
                                consumer_category=row[25], ws_case_size=row[26], kiosk_ship_qty=row[27], pick_station=row[28], fc_title=row[29],
                                width_space=row[30], height_space=row[31], depth_space=row[32], slotted_width=row[33], tag_volume=row[34],
                                delivery_option=row[35], tag_applied_by=row[36])
                db.session.add(query)
        try:
            db.session.commit() # aren't added until this is called
            result = "Import Successful {} records processed".format(count)
            print(result)
            flash(result)
            return redirect(url_for('main.index'))
        except IntegrityError as e:
            result = "Integrity Error {}".format(e)
            print(result)
            flash("Data Import Already Complete")
            return redirect(url_for('main.index'))
    except IOError as e:
        flash("Error connecting to csv for import")
        print(e)
        return redirect(url_for('main.index'))
