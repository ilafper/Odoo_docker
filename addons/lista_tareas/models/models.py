from odoo import models, fields, api

class ListaTareas(models.Model):
    #nombre y descripcion del modulo.
    _name = 'lista_tareas.lista_tareas'
    _description = 'Modelo de tareas'

    tarea = fields.Char(string='Tarea')
    prioridad = fields.Integer(string='Prioridad')
    urgente = fields.Boolean(string='Urgente', compute='_compute_urgente', store=True)
    realizada = fields.Boolean(string='Realizada')

    #añadido lo de la fecha limite en la base de datos, el "fields.date" indica el tipo de dato que es el campo en este caso fecha.
    fecha_limite = fields.Date(string='Fecha Límite')

    #añadir usuarios a la tarea.
    usuario_reponsable = fields.Many2many('res.users', string='Responsables')

   
    @api.depends('prioridad')

    def _compute_urgente(self):
        for record in self:
            if record.prioridad>10:
                record.urgente = True
            else:
                record.urgente = False


