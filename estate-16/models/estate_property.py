from odoo import fields,models
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"
    _order = "id desc"
    _sql_constraints = [
        ("expected_price", "check(expected_price >= 0)", "The Expected Price Must Be Strictly Positive"),
    ]
    _sql_constraints = [
        ("selling_price_", "check(selling_price >= 0)", "The Selling Price Must Be Strictly Positive"),
    ]
    
    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False,default = lambda self : fields.datetime.now()+relativedelta(months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default = 2)
    living_area = fields.Integer(string="Living Area (sqm)")
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer(string="Garden Area (sqm)")
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[('north', 'North'), ('south', 'South'), ('west', 'West'), ('east', 'East')]
    )
    active = fields.Boolean()
    state = fields.Selection(
        string='Status',
        selection=[('new', 'New'), ('offer_received', 'Offer Received'), ('offer_accepted', 'Offer Accepted'),
                   ('sold', 'Sold'), ('canceled', 'Canceled')],
        default='new',
        copy=False,
        required=True
    )
