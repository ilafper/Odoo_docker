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
        
        ancho=int(ancho)
        alto=int(alto)


        imagen = Image.new('RGB',(ancho,alto))

        #coger los pixeles de la imagen para luego añadirles color
        pixeles = imagen.load()

        for eje_x in range(ancho):
            for eje_y in range(alto):
                rojo=random.randit(0,255)
                verde=random.randit(0,255)
                azul=random.randit(0,255)
                pixeles[eje_x, eje_y] = (rojo, verde,azul)


        buffer = io.BytesIO()
        
         

    
    
