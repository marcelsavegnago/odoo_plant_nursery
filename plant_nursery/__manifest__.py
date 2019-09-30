# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Plant Nursery',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Plants and Customers Management',
    'depends': ['web', 'mail', 'rating', 'utm', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'views/assets.xml',
        'views/nursery_menus.xml',
        'views/nursery_plant_views.xml',
        'views/nursery_customer_views.xml',
        'views/nursery_order_views.xml',
        'views/rating_rating_views.xml',
        'views/nursery_plant_templates.xml',
        'views/nursery_plant_quote_ask.xml',
        'data/ir_sequence_data.xml',
        'data/mail_template_data.xml',
        'security/security.xml',
    ],
    'demo': [
    ],
    'css': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
