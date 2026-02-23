{
    'name': 'Sales Custom',
    'summary': 'Sales Custom module',
    'version': '1.0',
    'category': 'Uncategorized',
    'description': """ sales custom module""",
    'author': 'Mycompany',
    'website': 'https://www.mycompany.com',
    'depends': ['sale'],
    'data':[
        # 'security/ir.model.access.csv',
        'views/sales_custom_view.xml',
    ],
    'installable':True,
    'auto_install':False,
    'application': False,
}