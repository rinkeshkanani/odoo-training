# -*- coding: utf-8 -*-
{
    'name': 'Sale Order Wizard',
    'version': '1.0',
    'summary': 'Brief description of the module',
    'description': '''
        Detailed description of the module
    ''',
    'category': 'Uncategorized',
    'author': '',
    'company': '',
    'maintainer': '',
    'website': '',
    'depends': ['base', 'sale', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_invoice.xml',
        'views/sale_order_wizard_views.xml',
        'views/sale_wizard.xml',
        'data/sale_schedule_view.xml',
        'data/sale_quotation_schedule_view.xml',
        'data/risk_level_server.xml',
        'data/sale_order_confirm_email.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
