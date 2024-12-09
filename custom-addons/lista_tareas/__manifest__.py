# -*- coding: utf-8 -*-
{
    'name': "lista_tareas",

    'summary': "Administrador de lista de tareas",

    'description': """
Lista de tareas en desarrollo
    """,

    'author': "Iballa",
    'website': "https://www.iballa.com",
    'application': True,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
}
