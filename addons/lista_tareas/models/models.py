from odoo import models, fields, api

class ListaTareas(models.Model):
    #nombre y descripcion del modulo.
    _name = 'lista_tareas.lista_tareas'
    _description = 'Modelo de tareas'

    tarea = fields.Char(string='Tarea')
    prioridad = fields.Integer(string='Prioridad')
    urgente = fields.Boolean(string='Urgente', compute='_compute_urgente', store=True)
    realizada = fields.Boolean(string='Realizada')
    #Este computo depende de la variable prioridad

    @api.depends('prioridad')

    def _compute_urgente(self):
        for record in self:
            if record.prioridad>10:
                record.urgente = True
            else:
                record.urgente = False
