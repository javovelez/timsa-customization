# -*- coding: utf-8 -*-
{
    'name': "sales_timsa",

    'summary': """
        Adecuacíon de la aplicación de ventas para el flujo de trabajo de Timsa
""",

    'description': """
        Adecuacíon de la aplicación de ventas para el flujo de trabajo de Timsa

    """,

    'author': "timsa ",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management','project','stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
