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
    
    # Métodos para los botones - ahora modificamos la prioridad
    def toggle_urgente(self):
        """Alternar el estado urgente cambiando la prioridad"""
        for record in self:
            if record.prioridad <= 10:
                record.prioridad = 15  
            else:
                record.prioridad = 5  
    
    def toggle_realizada(self):
        """Alternar el estado realizada"""
        for record in self:
            record.realizada = not record.realizada
