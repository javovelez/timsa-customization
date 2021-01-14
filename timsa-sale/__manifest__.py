# -*- coding: utf-8 -*-
{
    'name': "timsa_sale",

    'summary': """
       Parametrización de ventas TIMSA""",

    'description': """
        Agraga campo
    """,

    'author': "Javo",
    'website': "www.timsasa.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','l10n_ar','sale'],

    # always loaded
    'data': [
        'views/timsa_sale_form_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        
    ],
}
