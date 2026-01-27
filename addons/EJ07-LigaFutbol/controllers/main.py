# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

#Clase del controlador web
class Main(http.Controller):
    #Decorador que indica que la url "/ligafutbol/equipo/json" atendera por HTTP, sin autentificacion
    #Devolvera texto que estará en formato JSON
    #Se puede probar accediendo a http://localhost:9001/ligafutbol/equipo/json     (en mi caso es 9001 por lo mapeo en la originar es el por defecto 8069)
    @http.route('/ligafutbol/equipo/json', type='http', auth='none')
    def obtenerDatosEquiposJSON(self):
        #Obtenemos la referencia al modelo de Equipo
        equipos = request.env['liga.equipo'].sudo().search([])
        
        #Generamos una lista con informacion que queremos sacar en JSON
        listaDatosEquipos=[]
        for equipo in equipos:
             listaDatosEquipos.append([equipo.nombre,str(equipo.fecha_fundacion),equipo.jugados,equipo.puntos,equipo.victorias,equipo.empates,equipo.derrotas])
        #Convertimos la lista generada a JSON
        
        json_result=json.dumps(listaDatosEquipos)

        return json_result
    



    #Se puede probar accediendo a http://localhost:9001/ligafutbol/eliminarempates
    @http.route('/ligafutbol/eliminarempates', type='http', auth='none')
    #funcion para eliminar los empates
    def eliminarEmpates(self):
       
        try:
            #acceder al modelo odoo para los partidos
            Partido = request.env['liga.partido']
            #meter todos los partidos en una lista, lo que haria el sudo() sseria acceder a todos los datos ignorando los permisos, seria como la consulta de select * from tabla; (mostrar todos los datos de la tabla ) 
            todos_partidos = Partido.sudo().search([])
            #lista vacia para ir guardando los empates
            lista_empates=[]
            # info de los empates a eliminar para luego mostrar
            lista_info_empates=[]
            

            # recorrer todos los partidos
            for partido in todos_partidos:
                
                
                partido_info = {
                    "id": partido.id,
                    "local": partido.equipo_casa.nombre,
                    "goles_local": partido.goles_casa,
                    "visitante": partido.equipo_fuera.nombre,  
                    "goles_visitante": partido.goles_fuera,
                    "resultado": f"{partido.goles_casa}-{partido.goles_fuera}",
                }
                
                if partido.goles_casa == partido.goles_fuera:
                    lista_empates.append(partido)
                    lista_info_empates.append(partido_info)  
            
                #total de empates
                total_empates=len(lista_empates)
                
            if total_empates> 0:
                for cada_empate in lista_empates:
                    cada_empate.unlink()
            
                respuesta={
                    "menssage": "se han eliminado los partidos en empate",
                    "total partidos eliminados": total_empates,
                    "info partidos eliminados": lista_info_empates
                }
            else:
                respuesta = {
                    "message": "No hay partidos en empate para eliminar",
                    "Nº partidos eliminados": 0
                }

            return json.dumps(respuesta)

            
            
        except Exception as e:
            return json.dumps({"error": str(e)})
            
