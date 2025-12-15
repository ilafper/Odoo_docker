from odoo import models, fields, api

class ListaTareas(models.Model):
    _name = 'lista_tareas.lista_tareas'
    _description = 'Modelo de tareas'
    
    _rec_name = 'tarea'
    tarea = fields.Char(string='Tarea')
    prioridad = fields.Integer(string='Prioridad')
    urgente = fields.Boolean(string='Urgente', compute='_compute_urgente', store=True)
    realizada = fields.Boolean(string='Realizada')

    #añadido lo de la fecha limite en la base de datos, el "fields.date" indica el tipo de dato que es el campo en este caso fecha.
    fecha_limite = fields.Date(string='Fecha Límite')

    #añadir usuarios a la tarea, relacion de muchosa muchos,
    usuario_reponsable = fields.Many2many('res.users', string='Responsables')
    
   
    deadline = fields.Date(string='Fecha Límite')

    @api.depends('prioridad')
    def _compute_urgente(self):
        for record in self:
            record.urgente = record.prioridad > 10
    
