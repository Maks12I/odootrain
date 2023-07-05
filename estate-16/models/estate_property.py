from odoo import fields,models
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"
    _order = "id desc" 

    
    name = fields.Char(required=True)
    property_type_id = fields.Many2one('estate.property.type', string = "Property Type")
    description = fields.Text()
    postcode =  fields.Char()
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
