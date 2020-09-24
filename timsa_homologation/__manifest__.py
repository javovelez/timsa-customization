# -*- coding: utf-8 -*-
{
    'name': "timsa_homologation",

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
        'data/cuit.xml',
        'data/cartificate_homo.xml'
        'data/parameter_homo.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        
    ],
}
