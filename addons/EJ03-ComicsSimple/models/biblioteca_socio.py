from odoo import models, fields, api


class Socio(models.Model):
    _name = 'biblioteca.socio'
    _description = 'Socio biblioteca prueba'

    _rec_name = 'nombre'
    #campo de nombre del socio
    nombre = fields.Char(string='Nombre')
    #campo apellidd del socio
    apellido = fields.Char(string='Apellido')
    #identificador unico del socio
    identificador = fields.Char(string='Identificador', required=True)


    _sql_constraints = [
        ('identificador_uniq', 'UNIQUE (identificador)', 'El identificador del socio debe ser único.')
    ]