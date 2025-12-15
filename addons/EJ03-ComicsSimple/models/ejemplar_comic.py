from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date



class EjemplarComic(models.Model):
    _name:'biblioteca_ejemplar'
    
    _description = 'Ejemplar de Comic para prestamo'

    #relacion de muchos a muchos , un comic puede tener varios ejemplaress
    comic_id=fields.Many2one('biblioteca.comic', String='Comic', required=True)

