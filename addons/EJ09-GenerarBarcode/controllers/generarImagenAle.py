# -*- coding: utf-8 -*-
# Importamos clases necesarias de Odoo para definir controladores HTTP
from odoo import http
from odoo.http import request
import random
from PIL import Image, ImageDraw
import io
import base64





# Clase controladora para las rutas HTTP que expone nuestro módulo
class ImagenAleatoria(http.Controller):


    #Se puede probar accediendo a http://localhost:9001/generador/imagenale
    
    # Ejemplo url http://localhost:9001/generador/imagenaleatoria?ancho=400&alto=400
    @http.route('/generador/imagenaleatoria', auth='public', cors='*', type='http')
    def generarImagenAleatoria(self, ancho,alto):
        #pasar los parametros que mandas a numero
        ancho=int(ancho)
        alto=int(alto)

        # creas como la plantilla de la imagen o lienza, el recuadro de la imagen del tamaño que le pasas
        
        imagen = Image.new('RGB',(ancho,alto))

        #coger los pixeles de la imagen para luego añadirles color
        pixeles = imagen.load()
        #recorrer la altura y lo alto de la imagen y pintar los pixeles de forma aleatoria
        for eje_x in range(ancho):
            for eje_y in range(alto):
                rojo=random.randint(0,255)
                verde=random.randint(0,255)
                azul=random.randint(0,255)
                pixeles[eje_x, eje_y] = (rojo, verde,azul)

        #guarda la imagen en memoria
        buffer = io.BytesIO()

        #cuado le des a guardar la imagen te saldra en formato png
        imagen.save(buffer, format='PNG')
        #  la parte base64.64encode convierte bytes binarios en texto seguro que puede ir en URLs/HTML.
        imagen_convertida = base64.b64encode(buffer.getvalue()).decode('utf-8')
        
        #devolver la imagen
        return f'<img src="data:image/png;base64,{imagen_convertida}">'
        

    
    
