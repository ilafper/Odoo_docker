# -*- coding: utf-8 -*-
#Este es el archivo principal
{
    'name': "lista_tareas_desesperacion2",
    'summary': "Sencilla lista de tareas",
    'description': """
        Módulo para gestionar tareas simples con prioridad y estado.
    """,
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    #a que categoria pertenece
    'category': 'Productivity',
    'version': '0.1',
    #indicar los modulos que dependa, en este caso solo del  base, no depende de ninguno en concreto.

    'depends': ['base'],
    
    'data': [
    'security/ir.model.access.csv',
    #cargar la vista del modulo
    'views/views.xml',
    
    ],

    'installable': True,
    'application': True,

}
