from odoo import models, fields, api
from odoo import models, fields, api

class ListaTareas(models.Model):
    _name = 'lista_tareas.lista_tareas'
    _description = 'Modelo de tareas'

    tarea = fields.Char(string='Tarea')
    prioridad = fields.Integer(string='Prioridad')
    urgente = fields.Boolean(string='Urgente', compute='_compute_urgente', store=True)
    realizada = fields.Boolean(string='Realizada')
    deadline = fields.Date(string='Fecha Límite')

    @api.depends('prioridad')
    def _compute_urgente(self):
        for record in self:
            record.urgente = record.prioridad > 10
    
   
