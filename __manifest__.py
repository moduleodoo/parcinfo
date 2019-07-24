# -*- coding: utf-8 -*-
{
    'name': "parc informatique",

    'summary': """
        requete informatique""",

    'description': """
        obtention d'un matériel informatique 
    """,

    'author': "Mes products",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'human Resources',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'product', ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/articles.xml',
        'views/entrepots.xml',
        'views/fournisseurs.xml',
        'views/requetes.xml',
        'views/utilisateurs.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}