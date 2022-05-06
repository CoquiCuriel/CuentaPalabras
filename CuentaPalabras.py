# -*- coding: utf-8 -*-
"""
Created on Fri May  6 18:56:30 2022

@author: Ricardo Curiel
"""

cadena = "cadena de prueba para contar palabras"

#len() cuenta cada caracter
cantidad = len(cadena)
print(cantidad)

#-----------------------------------------------------

texto = input("cuentame algo, lo que quieras") 
#len + str + split 
#len(str.split())
#cuenta cada palabra en una cadena (por defecto toma en cuenta los espacios)
cantidad = len(texto.split())
print(f"me has contado todo eso en {cantidad} palabras.")
