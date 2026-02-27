# -*- coding: utf-8 -*-
{
    "name": "Real Estate",
    "version": "19.0.1.0.0",
    "category": "Tools",
    "summary": "",
    "description": "",
    "author": "",
    "maintainer": "",
    "website": "",
    "depends": ["base", "mail", "contacts"],
    "data": [
        "security/ir.model.access.csv",
        "data/ir_sequence_data.xml",
        "data/ir_cron_data.xml",
        "views/real_estate_views.xml"
    ],
    "demo": [
        "demo/real_estate_data.xml"
    ],
    "assets": {
        'web.assets_backend': [
            'real_estate/static/src/js/client_action.js',
            'real_estate/static/src/xml/client_action.xml',
            'https://www.gstatic.com/charts/loader.js'
        ]
    },
    "license": "LGPL-3",
    "installable": True,
    "auto_install": False,
    "application": True
}