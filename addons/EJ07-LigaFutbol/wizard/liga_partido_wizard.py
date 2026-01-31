# -*- coding: utf-8 -*-
from odoo import models, fields

class LigaPARTIDOWizard(models.TransientModel):
    #Nombre y descripcion del modelo que hace referencai
    _name = 'liga.partido.wizard'

    _description = 'Wizar para registrar partido nuevo'

    #Campos del modelo que usaremos

    equipo_casa= fields.Many2one('liga.equipo', string= 'Equipo  local', required= True)
    equipo_fuera= fields.Many2one('liga.equipo', string= 'Equipo  visitante', required= True)
    
    goles_fuera= fields.Integer(string= 'goles Equipo  local', default= 0)
    goles_casa= fields.Integer(string= 'goles equipo casa', default= 0)

    #nuevo campo de jornada
    jornada= fields.Integer('jornada', default=1, required=False)

    #Funcion que se llamara desde el Wizard, para utilizando este modelo temporal
    #y con el crear un nuevo registro en el modelo destino
    def crear_partido_wizard(self):
        #Obtenemos referencia al modelo destino

        modeloDestino = self.env['liga.partido']
        #Tenemos que recorrer porque recordamos self referencia a todo el modelo
        for wiz in self:
            #Por cada elemento (en verdad, este Wizars solo tendra uno)
            #Creamos un registro en "liga.equipo"
            modeloDestino.create({
                #tenemos que especificar el id de cada equipo por
                # que si no salta error al crear los partidos
                'equipo_casa': wiz.equipo_casa.id,
                'equipo_fuera': wiz.equipo_fuera.id,
                'goles_casa':wiz.goles_casa,
                'goles_fuera':wiz.goles_fuera,
                'jornada':wiz.jornada
            })
        #Finalmente, recargamos la vista para ver el nuevo partido, esto hara 
        # que se recargue automaticamente al crear el partido
        return{'type':'ir.actions.client', 'tag':'reload'}