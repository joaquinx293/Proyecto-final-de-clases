
import csv
import random
import numpy as np


class Comunidad:
    def __init__(self, num_ciudadanos, promedio_conexion_fisica, probabilidad_conexion_fisica):
        self.num_ciudadanos = num_ciudadanos
        self.promedio_conexion_fisica = promedio_conexion_fisica
        self.probabilidad_conexion_fisica = probabilidad_conexion_fisica
        self.personas = []
    
    def cargar_personas_desde_csv(self, archivo_csv):
        with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.personas.append({
                    'Nombre': row['Nombre'],
                    'Apellido': row['Apellido'],
                    'ID': row['ID'],
                    'Estado': 'Sano', 
                    'familia': row['Apellido'],
                    'Conexiones': [],
                    'ConexionesFamiliares': [],
                    'Contador': 0 
                })
        return self.personas
    
    def numero_personas(self):
        return len(self.personas)
    
    def crear_conexiones(self):
        for persona in self.personas:
            num_conexiones = int(np.random.normal(self.promedio_conexion_fisica, 1))
            num_conexiones = max(0, num_conexiones)
            if num_conexiones > len(self.personas) - 1:
                num_conexiones = len(self.personas) - 1
            conexiones = np.random.choice(self.personas, num_conexiones, replace=False)
            persona['Conexiones'] = [conexion['ID'] for conexion in conexiones]
            conexiones_familiares = [
                p['ID'] for p in self.personas 
                if p['familia'] == persona['familia'] and p['ID'] != persona['ID']
            ]
            persona['ConexionesFamiliares'] = conexiones_familiares
            

    def imprimir_estado(self):
        for persona in self.personas:
            print(f"Nombre: {persona['Nombre']}, Apellido: {persona['Apellido']}, ID: {persona['ID']}, Estado: {persona['Estado']}, Familia: {persona['familia']}")
