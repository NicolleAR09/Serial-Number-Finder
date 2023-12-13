#Abrir archivos zip

import shutil
import os
from datetime import date
import re
import time
import math
from pathlib import Path

#shutil.unpack_archive('Proyecto+Dia+9.zip', 'Proyecto dia 9', 'zip')

#Buscador de números de serie

inicio = time.time()
patron = r'N\D{3}-\d{5}'
ruta = "C:\\Users\\Usuario\\Documents\\Udemy\\Python GitHub\\Serial Number Finder\\Proyecto dia 9\\Mi_Gran_Directorio"
lista_archivos = []
lista_numeros = []


def texto_patron():
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for arch in archivo:
            arch1 = open(Path(carpeta,arch), 'r')
            arch1 = arch1.read()
            if re.search(patron, arch1):
                resultado = re.search(patron, arch1)
                lista_archivos.append(arch.title())
                lista_numeros.append(resultado.group())



def inicio_codigo():
    i = 0
    fecha = date.today()
    print('-' * 50)
    print(f"Fecha de búsqueda: {fecha.day}/{fecha.month}/{fecha.year}")
    print('ARCHIVO', '\t' * 2, 'NRO. SERIE')
    print('-' * 7, '\t' * 2, '-' * 10)
    texto_patron()

    for arch in lista_archivos:
        print(f'{arch}\t {lista_numeros[i]}')
        i += 1
    final = time.time()
    tiempo = math.ceil(final - inicio)
    print(f'Número encontrados: {len(lista_numeros)}')
    print(f'Duración de la búsqueda: {tiempo} seg')
    print('-' * 50)
    print("\n")


inicio_codigo()