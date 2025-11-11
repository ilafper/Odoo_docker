# -*- coding: utf-8 -*-
{
    'name': "lista_tareas",
    'summary': "Sencilla lista de tareas",
    'description': """
        Módulo para gestionar tareas simples con prioridad y estado.
    """,
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Productivity',
    'version': '0.1',
    'depends': ['base'],
    
    'data': [
    'security/ir.model.access.csv',
    'views/views.xml',
    
    ],

    'installable': True,
    'application': True,

}
