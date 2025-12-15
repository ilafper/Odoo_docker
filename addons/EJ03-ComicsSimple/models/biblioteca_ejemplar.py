from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date



class EjemplarComic(models.Model):
    _name:'biblioteca.ejemplar'
    
    _description = 'Ejemplar de Comic para prestamo'

    #relacion de muchos a muchos , un comic puede tener varios ejemplaress
    comic_id=fields.Many2one('biblioteca.comic', String='Comic', required=True)

    socio_id= fields.Many2one('biblioteca.socio', Strinf='Socio')

    fecha_prestamo= fields.Date('Fecha de pretamo')

    fecha_devolucion= fields.Date('fecha de devolucion')

    estado=fields.Selection( [('disponible', 'Disponible'),
         ('prestado', 'Prestado')],
        string='Estado',
        default='disponible')
    
    #Comprobar que la fecha de prestamos no puede ser posterior al dia actual
    @api.constrains('fecha_prestamo')
    def comprobar_fecha_prestamo(self):
       for cada_registro in self:
          #comprobacion
          if cada_registro.fecha_prestamo and cada_registro.fecha_prestamo > date.today():
             #mensaje de error
             raise ValidationError("La fecha de prestamo no puede ser posterior al día actual.")


    @api.constrains('fecha_devolucion')
    def comprobar_fecha_devolucion(self):
        for cada_registro in self:
          #comprobacion
          if cada_registro.fecha_devolucion and cada_registro.fecha_devolucion < date.today():
             #mensaje de error
             raise ValidationError("La fecha de devolucion no puede ser inferior al día actual.")
          

    # Cambiar estado automáticamente si se asigna un socio
    @api.onchange('socio_id')
    def _onchange_socio(self):
        if self.socio_id:
            self.estado = 'prestado'
        else:
            self.estado = 'disponible'