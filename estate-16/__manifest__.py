# -*- coding: utf-8 -*-
# More info at https://www.odoo.com/documentation/master/reference/module.html

{
    "name": "Real Estate from tutorial",
    "depends": [
        "base"],
    'installable': True,
    'application': True,
# data files always loaded at installation
    'data': 
    [    'security/ir.model.access.csv',
'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_menus.xml'
    ],
    'license': 'LGPL-3',

}