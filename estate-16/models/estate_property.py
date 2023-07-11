from odoo import fields,models
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError

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
    
    name = fields.Char('Title', required=True)
    description = fields.Text('Description')
    postcode = fields.Char('Postcode')
    date_availability = fields.Date('Available From', copy=False,default = lambda self : fields.datetime.now()+relativedelta(months=3))
    expected_price = fields.Float('Expected price', required=True)
    selling_price = fields.Float('Selling price', readonly=True, copy=False)
    bedrooms = fields.Integer('Bedrooms',default = 2)
    living_area = fields.Integer(string="Living Area (sqm)")
    facades = fields.Integer('Facades')
    garage = fields.Boolean('Garage')
    garden = fields.Boolean('Garden')
    garden_area = fields.Integer(string="Garden Area (sqm)")
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[('north', 'North'), ('south', 'South'), ('west', 'West'), ('east', 'East')]
    )
    active = fields.Boolean('Active',)
    state = fields.Selection(
        string='Status',
        selection=[('new', 'New'), ('offer_received', 'Offer Received'), ('offer_accepted', 'Offer Accepted'),
                   ('sold', 'Sold'), ('canceled', 'Canceled')],
        default='new',
        copy=False,
        required=True
    )
    total_area = fields.Integer('Total area', compute='_compute_total_area')
    best_price = fields.Float('Best price', compute='_compute_best_price')

    property_type_id = fields.Many2one('estate.property.type', string='Property type')
    buyer_id = fields.Many2one('res.partner',string='Buyer',copy=False)
    salesman_id = fields.Many2one('res.users', string='Salesman', default=lambda self: self.env.user)
    tag_ids = fields.Many2many('estate.property.tag',string='Property tags')
    offer_ids = fields.One2many('estate.property.offer','property_id',string='Property offers')

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for record in self:
            record.best_price = max(
                record.offer_ids.mapped('price')
            ) if record.offer_ids else 0.0

    @api.onchange('garden')
    def _onchange_garden(self):
        self.garden_area = 10 if self.garden else 0
        self.garden_orientation = 'north' if self.garden else False

    def action_sold_property(self):
        for record in self:
            if record.state == 'cancelled':
                raise UserError('Cancelled properties cannot be sold.')
            record.state = 'sold'

    def action_cancel_property(self):
        for record in self:
            if record.state == 'sold':
                raise UserError('Sold properties cannot be cancelled.')
            record.state = 'cancelled'
