# -*- coding: utf-8 -*-
{
    'name': "timsa_account",

    'summary': """
       Parametrización de TIMSA""",

    'description': """
        
    """,

    'author': "Javo",
    'website': "www.timsasa.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','l10n_ar'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/timsa_company_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        
    ],
}
