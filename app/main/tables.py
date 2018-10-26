from flask_table import Table, Col, LinkCol, ButtonCol


class Results(Table):

    id = Col('id')
    title = Col('Title')
    description = Col('Description')
    price = Col('Price')
    shelf_time = Col('Shelf Time')
    category_names = Col('Category names')
    vendor = Col('Vendr')
    source = Col('Source')
    delivery_option = Col('Delivery Option')
    view = LinkCol('View', 'main.read_product', url_kwargs=dict(id='id'))
    edit = LinkCol('Edit', 'main.update_product', url_kwargs=dict(id='id'))
    delete = LinkCol('Delete', 'main.delete_product', url_kwargs=dict(id='id'))

